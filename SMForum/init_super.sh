#!/bin/sh

echo "------ create default admin user ------"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('arad4228', 'arad4228@gmail.com', '4228')" | python manage.py shell