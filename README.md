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