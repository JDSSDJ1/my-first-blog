# Generated by Django 2.2.13 on 2020-08-08 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0010_auto_20200724_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='part',
        ),
    ]
