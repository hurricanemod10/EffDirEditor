# EffDirEditor

EffDirEditor is a Python project that re-implements three original MATLAB scripts 
(`ReadEffDir.m`, `WriteEffDir.m`, and `IsolateEff.m`) line by line in Python.  
The goal is to provide a cross-platform, standalone **EffDir Editor** that can be 
packaged into an `.exe` for Windows.

## Features
- Read `.effdir` binary files into a structured Python object (`read_effdir.py`)
- Write structured data back into `.effdir` format (`write_effdir.py`)
- Isolate and extract single effects from an `.effdir` (`isolate_eff.py`)
- A `main.py` script to tie everything together in a command-line interface

## Usage
Once built into an executable, the tool will allow users to:
- Open existing `.effdir` files
- Extract and edit specific effects
- Save modified `.effdir` files

## Build
This project includes a GitHub Actions workflow to automatically package the 
Python scripts into a Windows `.exe` using **PyInstaller**.  
When you push changes to this repository, the `.exe` will be built in the cloud 
and provided as a downloadable artifact.

## License
No license yet — private use only.

