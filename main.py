#!/usr/bin/python
# -*- coding: utf-8 -*-

import xlrd
import xlwt
import pathlib
import os


initFile = "init.xls"


def getPath(path=""):
    return os.path.join(*path.replace("\\", "/").split("/"))


def isTargetNormal(init, target=""):
    return pathlib.PurePath(target) in list(map(pathlib.PurePath, init["normal"]))


def checkFileExists(filename=""):
    path = getPath(filename)

    if not pathlib.Path(path).exists():
        print("There is no file with the given name '{}'".format(path))
        return False
    else:
        return True


def getNoteList(notes=""):
    note_list = notes.replace(" ", "").split(",")
    if len(note_list) == 1 and note_list[0] == "":
        note_list = [0]
    else:
        note_list = list(map(int, note_list))

    return note_list


def getName(name=""):
    return " ".join(map(str.capitalize, name.split()))


def getInit(filename=""):
    filename = getPath(filename)

    if not checkFileExists(filename):
        return None

    sheet = xlrd.open_workbook(filename, encoding_override="utf-8").sheet_by_index(0)

    init = {
        "normal": list(map(str.strip, sheet.cell_value(0, 1).split(","))),
        "target": list(map(str.strip, sheet.cell_value(1, 1).split(","))),
        "range": {
            "from": sheet.cell_value(3, 2),
            "to": sheet.cell_value(3, 3)
        },
        "save": sheet.cell_value(0, 4),
        "fio": [],
        "lesson": []
    }

    for i in [i for i in range(sheet.nrows) if i > 3]:
        fio = sheet.row_values(i)[0]
        lesson = sheet.row_values(i)[1]
        if fio != "":
            init["fio"].append(fio.upper())

        if lesson != "":
            init["lesson"].append(lesson.upper())

    return init


def doNormalFile(init, path=""):

    path = getPath(path)

    if not checkFileExists(path):
        return None

    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_index(0)

    targets = []

    for nrow in range(sheet.nrows):
        val = sheet.row_values(nrow)[0]
        if val.upper() in init["fio"]:
            targets.append((nrow + 1, getName(val)))

    peoples = dict()

    for row, name in targets:
        note = dict()

        for i in range(row, sheet.nrows):
            val = sheet.row_values(i)
            if val[0] != "":
                break

            note[val[1]] = getNoteList(val[2])

        peoples[name] = note

    return peoples


def doTargetFile(init, filename=""):
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)

    lesson = sheet.cell_value(2, 1).split("/")[0].replace(u"Потоки", "").strip()
    peoples = dict()

    for row in range(sheet.nrows):

        if sheet.cell_value(row, 0).upper() in init["fio"]:
            peoples[getName(sheet.cell_value(row, 0))] = (
                lesson,
                getNoteList(sheet.cell_value(row + 1, 2))
            )
            continue

    return peoples


def iterOverTargets(init):
    targets = []
    for files in [list(pathlib.Path(d).glob("*.xls")) for d in init["target"]]:
        for f in files:
            if isTargetNormal(init, f):
                continue
            targets.append(doTargetFile(init, f))

    return targets


def saveToXls(normals, targets, path="tmp.xls"):
    def notes_to_str(notes):
        return ", ".join(map(str, notes))

    def avg(notes):
        return sum(notes) / len(notes)

    def yoba(kv):
        return kv[0], notes_to_str(kv[1]), sum(kv[1]) / len(kv[1])

    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("result", cell_overwrite_ok=True)
    sheet.col(0).width = 5000
    sheet.col(1).width = 7000
    sheet.col(2).width = 10000

    pos = 0
    for name, lessons in normals[0].items():
        sheet.write(pos, 0, name)
        for i, kv in enumerate(lessons.items(), start=pos):
            lesson, notes, avg = yoba(kv)
            sheet.write(i + 1, 1, lesson)
            sheet.write(i + 1, 2, notes)
            sheet.write(i + 1, 3, avg)

        for t in targets:
            i += 1
            lesson, notes, avg = yoba(t[name])
            sheet.write(i, 1, lesson)
            sheet.write(i, 2, notes)
            sheet.write(i, 3, avg)

        pos = i + 2

    book.save(path)


if __name__ == '__main__':
    init = getInit(initFile)
    normals = [doNormalFile(init, f) for f in init["normal"]]
    targets = iterOverTargets(init)

    saveToXls(normals, targets, init["save"])
