# -*- coding: utf-8 -*-

# A very simple setup script to create a single executable
#
# hello.py is a very simple 'Hello, world' type script which also displays the
# environment in which the script runs
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the script without Python

from cx_Freeze import setup, Executable

executables = [
    Executable('Word-sys.py')
]

<<<<<<< HEAD
setup(name='Word-sys',
=======
setup(name='Word-os',
>>>>>>> cc1770e005174ca578568f6ae96f93531050af40
      version='0.1',
      description='Compiler For Work In Computer (Link In GitHub https://github.com/progprof/Word-sys)',
      executables=executables
      )
