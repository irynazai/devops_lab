## **Snapshot** package

## Description:
*System snapshots with information about CPU and memory usage.*

# Requirements:

*To use this package you need to install "wheel". Run command:*
- pip install wheel

*To build the package run:*
python setup.py bdist_wheel

# Installation:
- pip install .
- snapshot [-h] [-i I] [-t T]

*optional arguments:*
  -h, --help  show this help message and exit
  -i I        Interval between snapshots ( default = txt)
  -t T        Output file type ( default = 30s)

# Directory with snapshots file:
*The .json or .txt file will be saved to the "/tmp/snapshots/" directory.*

# Removing:
pip uninstall snapshot
