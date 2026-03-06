#!/usr/bin/env bash

python manage.py migrate

uvicorn api.main:app --host 0.0.0.0 --port $PORT