@echo off

REM Build *.exe file and all requirements libraries by cx_Freeze
python setup.py build_exe

REM Build an installation file by Inno Setup 5
compil32 /cc setup.iss
