# Generated by Django 2.2.19 on 2021-03-23 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0048_delete_duplicate_enrollments'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='', max_length=255),
        ),
    ]
