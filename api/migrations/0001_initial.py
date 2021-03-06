# Generated by Django 3.2.9 on 2021-11-06 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.BigIntegerField(unique=True)),
                ('station_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(unique=True)),
                ('password', models.CharField(max_length=16)),
                ('username', models.CharField(max_length=256)),
                ('date_created', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle_id', models.BigIntegerField(unique=True)),
                ('borrowed_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.user')),
                ('station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.station')),
            ],
        ),
    ]
