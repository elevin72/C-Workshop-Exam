#!/bin/bash

for directory in src/*/ ; do
	echo "building $directory"
	${1:-gcc} $directory/*.c -o $directory/${2:-a.out} -Wall -Werror
done
doxygen Doxyfile