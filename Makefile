# compiler
CC = gcc

# libraries to link (eg. "-lm", etc.)
LIBS =

# compiler flags
CFLAGS = -Wall -Werror

# source directory to build in
SOURCE_DIR = src

# Doxygen options
DOXYFILE = Doxyfile

# locate project directory
PROJECT_DIR = $(SOURCE_DIR)/$@

# gather the list of source files
SOURCES = $(wildcard $(PROJECT_DIR)/*.c)

all:
	python build.py

docs:
	doxygen $(DOXYFILE)

# compile all the source files in a given directory
%: $(SOURCES)
	$(CC) $(CFLAGS) $(LIBS) -o $(PROJECT_DIR)/a.out $(SOURCES)
