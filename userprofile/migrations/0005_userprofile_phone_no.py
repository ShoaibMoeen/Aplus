# Generated by Django 2.2.19 on 2021-03-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_auto_20200721_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone_no',
            field=models.CharField(default='', max_length=20),
        ),
    ]
