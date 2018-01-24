# -*- coding: utf-8 -*-


import argparse


def getParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", metavar="workingDir", required=True,
                        help="Наименование рабочей директории.")
    parser.add_argument("-o", metavar="outputFile", required=False,
                        help="Имя выходного файла.")

    return vars(parser.parse_args())
