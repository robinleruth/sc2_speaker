#!/bin/bash

export APP_ENV=test

source venv/bin/activate

clear

# python -m unittest tests/test_db.py
# python -m unittest tests/test_main_service.py
python -m unittest tests/test_param_service.py
