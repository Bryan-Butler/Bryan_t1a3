#!/bin/bash
python3 -m venv environment
source environment/bin/activate
pip install pytest
python3 -m pytest ./test.py
deactivate
rm -r environment