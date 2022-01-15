# Simple python gui form json creator

## Prerequisites

You should have python v 3.7 or newer

### Install Tkinter

`pip install tk`  
`pip3 install tk`

### Install Pyinstaller

`pip install pyinstaller`  
`pip3 install pyinstaller`

### Install via requirements.txt

`pip install -r ./requirements.txt`  
`pip3 install -r ./requirements.txt`

## Starting the application

### Run manually

`python main.py`  
`python3 main.py`

When the application starts, the _form_construction.json_ is loaded.  
This file contains the blueprint, what input fields should be shown and saved.

When the Add button gets clicked, the new configuration will be appended to _teaser.json_.  
If this file is not existant, a new will be created.


##Create binary executable
`pyinstaller main.py --onefile -n SimpleJsonForm`

After successful compilation, the following file can be run.  
Example:
`./dist/SimpleJsonForm`


