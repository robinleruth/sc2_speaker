#!/bin/bash

source venv/bin/activate

clear
python -m unittest discover tests
