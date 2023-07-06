#!/bin/bash
python3 -m venv test_environment

if [ -f "test_environment/Scripts/activate" ]; then
  source test_environment/Scripts/activate
else
  source test_environment/bin/activate
fi

pip install pytest
python3 -m pytest ./test.py
deactivate
rm -r test_environment