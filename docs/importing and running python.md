## Option 1:  run a module as the main program
* remember tha a file contining python code used by other parts of a package is a "module" even if it only has one line of code in it
* The code must be in the directory tree of the projects and this must be executed from the project root directory
* this will execute all of the code in that module, and is a good way to execute `__main__` code

To execute this you want to use the following syntax
```bash
python -m modulepath.modulename
```

* the `-m` means that it is searching for a module
* we give dots - `.` notatiion as this is how we define the paths as in an import statement.  
* there is no extension `.py` as we are refereing to it by its import path, not its filename

## Option 2: Execute a standalone script
```bash
python run_example_directly.py
```
In this case the code is not part of the package, and the code resides outside of the package.  