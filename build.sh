#!/usr/bin/env bash
# Error aane par script ruk jaye
set -o errexit

echo "Installing requirements..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating database migrations..."
python manage.py makemigrations

echo "Applying database migrations..."
python manage.py migrate

echo "Creating superuser (Admin account)..."
if [[ $CREATE_SUPERUSER ]];
then
  python manage.py createsuperuser --no-input --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL || true
fi

echo "Seeding all initial projects..."
python seed.py