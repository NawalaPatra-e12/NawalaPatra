# Generated by Django 4.2.6 on 2023-10-27 14:51

from django.db import migrations
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books1.json")

class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20231027_2145'),
    ]

    operations = [
        migrations.RunPython(load_my_initial_data),
    ]
