#!/bin/bash
source /home/www/code/second_test_task/env/bin/activate
exec gunicorn  -c "/home/www/code/second_test_task/backend/gunicorn_config.py" backend.wsgi
