#!/bin/sh
python -m autopep8 ipspot --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --max-line-length 120 --verbose
python -m autopep8 otherfiles --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --max-line-length 120 --verbose
python -m autopep8 setup.py --recursive --aggressive --aggressive --in-place --pep8-passes 2000 --max-line-length 120 --verbose
