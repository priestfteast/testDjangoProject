# Generated by Django 3.2.6 on 2021-09-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msgs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='msgform',
            name='variables_quantity',
            field=models.IntegerField(default=0),
        ),
    ]
