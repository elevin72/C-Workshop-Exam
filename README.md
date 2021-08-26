# C Workshop Exam

Exam solution for C Workshop course August 2021

## Documentation

[Documentation](https://abrahammurciano.github.io/C-Workshop-Exam/files.html)

## Visual Studio Code

The files [`.vscode/launch.json`](.vscode/launch.json) and [`.vscode/tasks.json`](.vscode/tasks.json) contain tasks to build and run the project.

### Debug an Exercise

To run and debug a single exercise, open any file in the exercise directory, then press <kbd>F5</kbd>.

Make sure that in [`.vscode/launch.json`](.vscode/launch.json) the option `"program"` is set to `"${fileDirname}/a.out"` where instead of `a.out` you have the name of the compiled binary (eg. `a.exe` for Windows).

Make sure that in this file you also have the option `"miDebuggerPath"` set to the path to `gdb` on your device.

In [`.vscode/tasks.json`](.vscode/tasks.json) in the task labelled `"C/C++: gcc build active folder"` make sure `"command"` is set to the path to your compiler, and the argument after `"-o"` is set to `"${fileDirname}/a.out"` where instead of `a.out` you have the name of the compiled binary (eg. `a.exe` for Windows).

### Build All Exercises and Documentation

There are tasks which wrap around the included Python and Bash build files. To execute them from VS Code, use the keyboard shortcut <kbd>CTRL</kbd> + <kbd>SHIFT</kbd> + <kbd>P<kbd> to bring up the command pallet. Then type `Tasks: Run Task` into the command pallet and press <kbd>Enter</kbd>. Finally choose "C/C++: gcc build all folders with bash" or "C/C++: gcc build all folders with python" to build all exercises as well as the documentation, or choose "Doxygen: Generate documentation" to only generate documentation.

For the Python and Bash tasks, make sure the second, third, and fourth arguments in `"args"` in the corresponding tasks in [`.vscode/tasks.json`](.vscode/tasks.json) are the path to your compiler, the name of the output file, and the name of the doxygen configuration file respectively.

For the task "Doxygen: Generate documentation", make sure the first argument in `"args"` is the name of the doxygen configuration file.

## Python and Bash Build Scripts

To build all exercises with the Python or Bash build scripts, run either of the following commands:

```
python build.py /bin/gcc a.out Doxyfile
```

or

```
bash build.sh /bin/gcc a.out Doxyfile
```

Replace `/bin/gcc` with the path to your compiler.
Replace `a.out` with whatever you'd like the compiled binary to be called (eg. `a.exe`).
Replace `Doxyfile` with the name of the doxygen configuration file.

## Makefile

You can use the makefile in one of the following ways.

### 1. To build all exercises and the documentation:

```
make all
```

or just

```
make
```

### 2. To build specific exercises

```
make Ex01
```

Where `Ex01` is the name of the folders inside `src/` containing the source files for one exercise.

**Note:** You can pass multiple exercises at a time, for example `make Ex01 Ex02`.

### 3. To generate the documentation

```
make docs
```

### 4. Any combination of the above

You can combine any of the make commands into one command that will perform all the necessary tasks. For example the following command will compile the exercises in `src/Ex01` and `src/Ex02` as well as generate the documentation for all the exercises.

```
make Ex01 Ex02 docs
```

## Authors

-   [Jonah Lawrence](https://www.github.com/DenverCoder1)
-   [Abraham Murciano](https://www.github.com/abrahammurciano)
