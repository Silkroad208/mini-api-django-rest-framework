# Generated by Django 2.1 on 2019-07-28 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='first_name',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='last_name',
            new_name='lastname',
        ),
    ]
