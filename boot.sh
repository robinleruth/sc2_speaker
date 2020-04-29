#!/bin/sh

source venv/bin/activate
export APP_ENV=prd

exec gunicorn -b localhost:5000 --access-logfile --error-logfile - application:app
