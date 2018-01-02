import sys

import requests.certs
from cx_Freeze import Executable, setup

'''
To compile type "py -3 setup.py build_exe" in comand prompt
'''

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup(
    name='Paragraph Adapter',
    version='0.1',
    description='',

    options={
        'build_exe': {
            'optimize': 2,
            'include_msvcr': True,
            'packages': ['os', 'sys', 'xlrd', 'xlwt', 'datetime'],
            'includes': [],
            'excludes': ['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            'include_files': [
                # to importing requests for freezing app
                (requests.certs.where(), 'cacert.pem')
            ],
            'silent': True,
        }
    },

    executables=[
        Executable(
            targetName='ParagraphAdapter.exe',
            script='main.py',
            excludes=['tkinter', 'QtSql', 'QtSvg', 'QtTest', 'QtWebKit', 'QtXml'],
            compress=True,
            base=base
        )
    ]
)
