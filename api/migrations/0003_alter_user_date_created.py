# Generated by Django 3.2.9 on 2021-11-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211106_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
