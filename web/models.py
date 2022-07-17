from django.db import models

# python manage.py makemigrations
# python manage.py migrate
# Create your models here.

# python3 manage.py makemigrations
# python3 manage.py migrate

class friends_info(models.Model):
    name = models.CharField(max_length=64)
    birthday = models.DateField(max_length=64)
    hobby = models.CharField(max_length=256)