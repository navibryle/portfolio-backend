# Generated by Django 3.1.5 on 2021-01-06 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]