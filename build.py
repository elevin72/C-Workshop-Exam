#!/bin/python

import os
import subprocess
from typing import Iterable
from functools import reduce
import sys

def c_files_in_dir() -> Iterable[str]:
    return filter(
        os.path.isfile,
        [
            filename
            for filename in os.listdir(".")
            if filename.endswith(".c")
        ],
    )

def build_dir(compiler_and_args: str):
    print("Building in ", os.getcwd())
    files = c_files_in_dir()
    cmd  = [*compiler_and_args.split(' ')] + [*files]
    print(reduce(lambda s1, s2: s1 + " " + s2, cmd))
    if files:
        subprocess.check_call(cmd)

def doxygen(config_file: str):
    print("doxygening")
    subprocess.run(["doxygen", config_file],capture_output=True)

def build_in_all_dirs_in(src_dir: str, compiler_and_args: str):
    os.chdir(src_dir)
    if all(os.path.isfile(file) for file in os.listdir(".")):
        build_dir(compiler_and_args)
    else:
        for dir in os.listdir("."):
            if os.path.isdir(dir):
                build_in_all_dirs_in(dir, compiler_and_args)
    os.chdir("..")

src_dir = sys.argv[1] if len(sys.argv) > 1 else "src"
compiler_and_args = sys.argv[2] if len(sys.argv) > 2 else "gcc -Wall"
build_in_all_dirs_in(src_dir, compiler_and_args)
doxygen(sys.argv[3] if len(sys.argv) > 3 else "dconfig")
