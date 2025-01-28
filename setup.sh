#!/bin/bash

# Build Dependencies
cd rizzsec
make

# Make a key
cd ..
python3 ./rizzsec/src/rizzsec-keygen.py -o ./key.key

