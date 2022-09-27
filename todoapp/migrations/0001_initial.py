# Generated by Django 3.2.8 on 2022-09-27 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=64, verbose_name='Имя проекта')),
                ('link', models.URLField(max_length=64, verbose_name='Ссылка на репозиторий')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Пользователи проекта')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проект',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1024, verbose_name='Текст заметки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoapp.project', verbose_name='Проект')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор заметки')),
            ],
            options={
                'verbose_name': 'Заметка',
                'verbose_name_plural': 'Заметка',
            },
        ),
    ]
