#!/bin/bash

# Azure startup script for Django
echo "Starting Django application..."

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Start the application
echo "Starting Gunicorn server..."
gunicorn --bind 0.0.0.0:8000 mysite.wsgi:application
