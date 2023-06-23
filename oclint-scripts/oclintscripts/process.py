#! /usr/bin/env python3

import subprocess
import sys

from oclintscripts import environment

def call(command):
    if command_exit_code := subprocess.call(command, shell=True):
        sys.exit(command_exit_code)

def j_flag(j=None):
    multiple_thread = environment.cpu_count()
    if environment.is_mingw32():
        multiple_thread = 1
    if j not in [None, 0]:
        multiple_thread = j
    return f' -j {str(multiple_thread)}'

def make(j=None):
    call(f'make{j_flag(j)}')

def ninja(j=None):
    if j not in [None, 0]:
        call(f'ninja{j_flag(j)}')
    else:
        call('ninja')
