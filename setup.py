# -*- coding: utf-8 -*-


import sys

# import requests.certs
from cx_Freeze import Executable, setup

'''
To compile type "python setup.py build_exe" in comand prompt
'''

base = 'Console'
if sys.platform == 'win32':
    base = 'Win32GUI'


setup(
    name='Paragraph Adapter',
    version='0.2',
    description='',

    options={
        'build_exe': {
            'optimize': 2,
            'include_msvcr': True,
            'packages': ['pathlib', 'xlrd', 'xlwt', 'argparse'],
            'includes': [],
            'excludes': ['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            'include_files': [],
            'silent': True,
        }
    },
    executables=[
        Executable(
            targetName='ParagraphAdapter' + '.exe' if sys.platform == 'win32' else '',
            script='main.py',
            base=base
        )
    ]
)
