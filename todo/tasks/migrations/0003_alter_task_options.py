# Generated by Django 5.1.4 on 2024-12-08 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('id', 'created_at'), 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
