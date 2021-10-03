command = '/home/www/code/second_test_task/env/bin/gunicorn'
pythonpath = '/home/www/code/second_test_task/backend/'
bind = '127.0.0.1:8001'
workers = 3
user = 'www'
limit_request_fields = 32000
limit_request_fields_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=backend.settings'
