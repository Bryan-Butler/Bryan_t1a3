#!/bin/bash
python3 -m venv environment

if [ -f "environment/Scripts/activate" ]; then
  source environment/Scripts/activate
else
  source environment/bin/activate
fi

python3 ./main.py
deactivate
rm -r environment