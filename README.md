# doc-to-renpy

A simple script to convert contents of a word doc to renpy text format.

Ensure you have python version 3.8.10

# Installation

1. Create virtual environment
```
python3 -m venv venv
```

2. Source virtual environment.

Sourcing for a specific OS [here](https://docs.python.org/3/library/venv.html#module-venv)

Linux
```
source venv/activate/bin
```

Windows
```
venv/Scripts/activate.bat
```

3. Install requirements
```
pip install -r requirements.txt
```

# How To Convert

1. Place word documents in `docx` directory
2. Run job
```
python index.py
```
3. Associated .rpy file should be the in `results` directory

# Testing

1. `python -m unittest discover`