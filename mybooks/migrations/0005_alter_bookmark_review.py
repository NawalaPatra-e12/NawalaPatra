# Generated by Django 4.2.6 on 2023-10-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0004_rename_user_profile_bookmark_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='review',
            field=models.TextField(blank=True, max_length=1000),
        ),
    ]
