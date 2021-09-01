# Doxygen options
DOXYFILE = dconfig

all: debug

release:
	python build.py src "gcc -Wall -Werror -O5"

debug:
	python build.py src "gcc -g -Wall -Werror"

# custom build a specific directory like this
Ex01:
	python build.py src/Ex01 "gcc -g -o outfile"

docs:
	doxygen $(DOXYFILE)

