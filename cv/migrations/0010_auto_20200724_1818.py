# Generated by Django 2.2.13 on 2020-07-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20200724_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='part',
            field=models.CharField(choices=[('PROFILE', 'profile'), ('CONTACT', 'contact'), ('EDUCATION', 'education'), ('EXPERIENCE', 'experience'), ('INTEREST', 'interests')], default='education', max_length=10),
        ),
    ]
