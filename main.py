#!/usr/bin/python
# -*- coding: utf-8 -*-


import cli
import prepare
import excel


if __name__ == '__main__':

    args = cli.getParser()
    init = prepare.getInit(args)

    outputFilePath = prepare.getOutputFilePath(args, init)
    commonFilePath = prepare.getCommonFilePath(init)
    init["commonFile"] = commonFilePath.name

    print("Установленны следующие параметры:\n\tВходной файл: {}\n\tРабочая директория: {}\n\tИмя выходного файла: {}".format(
        commonFilePath,
        init["workingDir"],
        outputFilePath
    ))

    outputBook = excel.getOutputBook()

    excel.process(
        excel.getCommonSheet(str(commonFilePath)),
        excel.getOutputSheet(outputBook),
        excel.getThreadedFilesSheets(prepare.getThreadedFilesList(init, commonFilePath))
    )

    outputBook.save(str(outputFilePath))
    input("Готово.\nНажмите любую клавишу...")
