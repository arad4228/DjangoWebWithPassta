#!/bin/sh

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('arad4228', 'admin@myapp.local', '4228')" | python manage.py shell
