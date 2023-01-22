# doc-to-renpy

A simple script to convert contents of a word doc to renpy text format.

Ensure you have atleast python version 3.8.10

# Installation

1. Create virtual environment
```
python3 -m venv venv
```

2. Source virtual environment.

Sourcing for a specific OS [here](https://docs.python.org/3/library/venv.html#module-venv)

Linux/MacOS
```
source venv/bin/activate
```

Windows
```
venv/Scripts/activate.bat
```

3. Install requirements
```
pip install -r requirements.txt
```

# Running Conversion (GUI)

To run the gui

1. `source venv/bin/activate`
2. `python index.py`

# Running Conversion (Quick Convert)

Make sure you are sourced into your virtual environment

1. Place word documents in `./quick_convert_data/docx` directory
2. Run quick conversion
```
python index.py --quick_convert
```
3. Converted .rpy file should be the in `./quick_convert_data/renpy` directory

# Building

Okay, how do I install it on other people's machine without downloading it. 
We can build with pyinstaller by constructing the binary files.

Resource for [--add-data](https://pyinstaller.org/en/stable/spec-files.html#adding-data-files) here

Linux/MacOS
```
pyinstaller index.py \
  --collect-data sv_ttk \
  --add-data="./gui/assets/*.png:./gui/assets/" \
  --add-data="./quick_convert_data/docx/*:./quick_convert_data/docx/" \
  --add-data="./quick_convert_data/renpy/*:./quick_convert_data/renpy/"
```

Windows
```
pyinstaller index.py \
  --collect-data sv_ttk \
  --add-data="./gui/assets/*.png;./gui/assets/" \
  --add-data="./quick_convert_data/docx/*;./quick_convert_data/docx/" \
  --add-data="./quick_convert_data/renpy/*;./quick_convert_data/renpy/"
```

We can run it by calling the binary file
1. `./dist/index/index`

# Logging

There are two levels of logging
1. `INFO`
1. `DEBUG`

`INFO` is on by default.

To get `DEBUG` logs, run the `--verbose` flag

Examples.
1. `python index.py --verbose`
2. `python index.py --quick_convert --verbose`

# Testing

Make sure you are sourced into your virtual environment

1. `python -m unittest discover`