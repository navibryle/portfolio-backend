# Generated by Django 3.1.5 on 2021-01-13 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restApp', '0003_auto_20210109_0239'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherdataset',
            name='temp_max',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]