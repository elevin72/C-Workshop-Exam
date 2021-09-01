# Doxygen options
DOXYFILE = dconfig

all: debug

release:
	python build.py src "gcc -Wall -Werror -O5"

debug:
	python build.py src "gcc -g -Wall -Werror"

Ex01:
	# command should be something like "gcc -g -o outfile"
	python build.py src/Ex01 "My custom compile command"

docs:
	doxygen $(DOXYFILE)

