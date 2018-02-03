#py -3.6 -m py2exe.build_exe Word-sys.py
python.exe setup.py build

echo "Compiled..."

MOVE /Y build\exe.win32-3.6\Word-sys.exe  Word-sys.exe  

MOVE /Y build\exe.win32-3.6\python36.dll  python36.dll  

MOVE /Y build\exe.win32-3.6\lib  lib  

echo "Copied..."

RMDIR /S /Q build

echo "Cleaned..."
