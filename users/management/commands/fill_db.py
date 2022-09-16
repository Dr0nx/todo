from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()

        for user in users:
            if user.email == 'dr0nx@yandex.ru' or \
                    user.email == 'kovbozh@gmail.com' or \
                    user.email == 'admin@yuga.ru':
                user.delete()

        test1 = User(username='ivan', first_name='Иван', last_name='Иванов', email='mail1@mail.ru')
        test1.save()
        test2 = User(username='petr', first_name='Петр', last_name='Петров', email='mail2@mail.ru')
        test2.save()

        User.objects.create_superuser(username='dr0n', first_name='Андрей', last_name='Божков',
                                      email='kovbozh@gmail.com', password='1')