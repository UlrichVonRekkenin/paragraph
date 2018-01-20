import xlrd
import xlwt
import pathlib
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", metavar="workingDir", required=True,
                        help="Наименование рабочей директории.")
    args = vars(parser.parse_args())

    init = {
        "workingDir": pathlib.Path(args["d"]).name,
    }

    outputFilePath = pathlib.Path(init["workingDir"]).joinpath(
        "{}_output.xls".format(init["workingDir"]))

    for i, f in enumerate([f for f in pathlib.Path(init["workingDir"]).glob("*.xls")], start=1):
        print("{}) {}".format(i, f))

    num = input("Укажите номер общего файла из списка ниже...\n")
    init["commonFile"] = [f for f in pathlib.Path(
        init["workingDir"]).glob("*.xls")][int(num) - 1].name

    commonFilePath = pathlib.Path(init["workingDir"]).joinpath(init["commonFile"])
    if not commonFilePath.is_file():
        print("There is no {} file...\nExit.".format(init["commonFile"]))
        quit(1)

    print("Установленны следующие параметры:\n\tВходной файл: {}\n\tРабочая директория: {}\n\tИмя выходного файла: {}".format(
        commonFilePath,
        init["workingDir"],
        outputFilePath
    ))

    commonSheet = xlrd.open_workbook(commonFilePath).sheet_by_index(0)

    if not pathlib.Path(init["workingDir"]).is_dir():
        print("There is no {} dir...\nExit.".format(init["workingDir"]))
        quit(1)

    threadedFiles = [f for f in pathlib.Path(init["workingDir"]).glob(
        "*.xls") if not pathlib.Path(f).samefile(commonFilePath)]
    threadedSheets = [xlrd.open_workbook(f).sheet_by_index(0) for f in threadedFiles]

    outputBook = xlwt.Workbook(encoding="utf-8")
    outputSheet = outputBook.add_sheet("result", cell_overwrite_ok=True)
    outputSheet.col(0).width = 5000
    outputSheet.col(1).width = 10000
    outputSheet.col(2).width = 6000

    border = xlwt.easyxf('border: left thin, right thin, top thin, bottom thin')
    center = xlwt.easyxf(
        'border: left thin, right thin, top thin, bottom thin; alignment: horiz centre')
    center_red = xlwt.easyxf(
        'border: left thin, right thin, top thin, bottom thin; alignment: horiz centre; font: color red')

    def writeLessonsAndNotes(sheet=None, val=[], pos=0):

        def checkNotes(sheet=None, notes="", pos=[0, 0]):
            def avg(notes=""):
                notes = list(map(int, notes.split(",")))
                return round(sum(notes) / len(notes), 1)

            if notes != "":
                sheet.write(pos[0], pos[1], avg(notes),
                            center if avg(notes) > 3 else center_red)
            else:
                sheet.write(pos[0], pos[1], "-", center)

        sheet.write(pos, 1, val[1], border)
        sheet.write(pos, 2, val[2], border)
        checkNotes(sheet, val[2], [pos, 3])

    # iter over rows in commonFile
    outPos = 0
    iterOverThread = False
    for nrow in range(8, commonSheet.nrows):
        val = commonSheet.row_values(nrow)

        if val[0] != "":
            name = val[0]
            iterOverThread = True
            if outPos > 0:
                outPos += 2
            outputSheet.write(outPos, 0, name)
            outputSheet.write(outPos, 1, commonSheet.cell(5, 1).value)
        else:
            outPos += 1
            writeLessonsAndNotes(outputSheet, val, outPos)

        # and then after each name iter over threadedSheets and break at matching name
        if iterOverThread:
            for sheet in threadedSheets:
                for nrowsheet in range(8, sheet.nrows):
                    if sheet.row_values(nrowsheet)[0] == name:
                        outPos += 1
                        writeLessonsAndNotes(outputSheet, sheet.row_values(nrowsheet + 1), outPos)
                    continue
        # 1st including
        iterOverThread = False

    outputBook.save(outputFilePath)
    print("Готово.")
