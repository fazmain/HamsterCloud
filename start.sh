#!/bin/bash
# Startup script for HamsterCloud Flask application

echo "Starting HamsterCloud Flask application..."
exec gunicorn --bind 0.0.0.0:8000 app:app
