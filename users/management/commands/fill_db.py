import os
import random
import string

from todo import settings
from users.models import User
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import sqlite3


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        User.objects.all().delete()

        for i in range(3):
            username = get_random_string(5).lower()
            email = ''.join(random.choice(string.ascii_letters.lower()) for _ in range(5)) + '@gmail.com'
            User.objects.create_user(username=username, email=email, password='321')

        User.objects.create_superuser(username='dr0n', first_name='Андрей', last_name='Божков',
                                      email='kovbozh@gmail.com', password='321')
