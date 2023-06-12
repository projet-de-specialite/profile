#!/bin/sh

# Wait for the database to be ready
echo "Waiting for database..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "Database is ready!"

# Apply database migrations
python manage.py migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
