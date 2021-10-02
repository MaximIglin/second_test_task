source /root/code/second_test_task/env/bin/activate
exec gunicorn -c "/root/code/second_test_task/backend/gunicorn_config.py" backend.wsgi
