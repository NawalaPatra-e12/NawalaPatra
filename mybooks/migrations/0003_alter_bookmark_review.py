# Generated by Django 4.2.6 on 2023-10-27 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybooks', '0002_alter_bookmark_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='review',
            field=models.TextField(blank=True),
        ),
    ]
