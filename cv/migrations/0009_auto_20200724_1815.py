# Generated by Django 2.2.13 on 2020-07-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_section_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='part',
            field=models.CharField(choices=[('Profile', 'PROFILE'), ('Contact', 'CONTACT'), ('Education', 'EDUCATION'), ('Experience', 'EXPERIENCE'), ('Interests', 'INTEREST')], default='Education', max_length=10),
        ),
    ]
