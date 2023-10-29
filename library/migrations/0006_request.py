# Generated by Django 4.2.6 on 2023-10-28 12:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.core.management import call_command


def load_my_initial_data(apps, schema_editor):
    call_command("loaddata", "books1.json")


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0005_book_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('book_title', models.CharField(max_length=255)),
                ('book_author', models.CharField(max_length=255)),
                ('reason', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RunPython(load_my_initial_data),
    ]
