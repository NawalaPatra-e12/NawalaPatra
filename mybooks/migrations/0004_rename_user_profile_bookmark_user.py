# Generated by Django 4.2.6 on 2023-10-27 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0003_alter_bookmark_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmark',
            old_name='user_profile',
            new_name='user',
        ),
    ]
