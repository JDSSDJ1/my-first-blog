# Generated by Django 2.2.13 on 2020-06-28 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_section_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='order',
        ),
    ]