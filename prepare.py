# -*- coding: utf-8 -*-


import pathlib


def getInit(args=None):
    path = pathlib.Path(args["d"]).name

    if not pathlib.Path(path).is_dir():
        print("Директория '{}' не существует...\nВыход.".format(path))
        quit(1)

    return {"workingDir": path}


def getCommonFilePath(init=None):
    for numFile, f in enumerate([f for f in pathlib.Path(init["workingDir"]).glob("*.xls")], start=1):
        print("{}) {}".format(numFile, f))

    num = input("Укажите номер общего файла из списка выше...\n")
    return [f for f in pathlib.Path(init["workingDir"]).glob("*.xls")][int(num) - 1]


def getOutputFilePath(args=None, init=None):
    return pathlib.Path(init["workingDir"]).joinpath("{}{}".format(
        pathlib.Path(args["o"]).name,
        "" if pathlib.Path(args["o"]).suffix else ".xls"
    )) \
        if args["o"] else \
        pathlib.Path(init["workingDir"]).joinpath(
        "{}_output.xls".format(init["workingDir"]))


def getThreadedFilesList(init=None, common=""):
    files = [str(f) for f in pathlib.Path(init["workingDir"]).
             glob("*.xls") if not pathlib.Path(f).samefile(common)]

    if not len(files):
        print("Предупреждение:\n\tВ директории {} не обнаружено файлов для потоков...")

    return files
