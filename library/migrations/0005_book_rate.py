# Generated by Django 4.2.5 on 2023-10-28 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20231027_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]
