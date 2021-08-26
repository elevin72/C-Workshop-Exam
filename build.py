#!/bin/python

import os
import subprocess
from typing import Iterable
import sys


def files_in(path: str = ".", ext="") -> Iterable[str]:
	return filter(
		os.path.isfile,
		[
			os.path.join(path, filename)
			for filename in os.listdir(path)
			if filename.endswith(ext)
		],
	)


def build_dir(path: str, outfile: str):
	files = files_in(path, ".c")
	if files:
		subprocess.check_call(
			["gcc", *files, "-o", os.path.join(path, outfile), "-Wall", "-Werror"]
		)


def doxygen(config_file: str):
	subprocess.check_call(["doxygen", config_file])


src = "src"
compiler = sys.argv[1] if len(sys.argv) > 1 else "gcc"
outfile = sys.argv[2] if len(sys.argv) > 2 else "a.out"
for directory in os.listdir(src):
	path = os.path.join(src, directory)
	if os.path.isdir(path):
		print("building", path)
		build_dir(path, outfile)
doxygen("Doxyfile")