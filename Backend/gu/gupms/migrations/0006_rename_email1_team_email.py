# Generated by Django 4.1.1 on 2022-11-08 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gupms', '0005_alter_team_regnumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='email1',
            new_name='email',
        ),
    ]