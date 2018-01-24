# -*- coding: utf-8 -*-


import xlrd
import xlwt

border = xlwt.easyxf('border: left thin, right thin, top thin, bottom thin')
center = xlwt.easyxf(
    'border: left thin, right thin, top thin, bottom thin; alignment: horiz centre')
center_red = xlwt.easyxf(
    'border: left thin, right thin, top thin, bottom thin; alignment: horiz centre; font: color red')


def process(commonSheet, outputSheet, threadedSheets=[]):
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


def getOutputBook():
    return xlwt.Workbook(encoding="utf-8")


def getOutputSheet(book=None):
    sheet = book.add_sheet("result", cell_overwrite_ok=True)
    sheet.col(0).width = 5000
    sheet.col(1).width = 10000
    sheet.col(2).width = 6000
    return sheet


def getCommonSheet(common=""):
    return xlrd.open_workbook(common).sheet_by_index(0)


def getThreadedFilesSheets(files=[]):
    return [xlrd.open_workbook(f).sheet_by_index(0) for f in files]
