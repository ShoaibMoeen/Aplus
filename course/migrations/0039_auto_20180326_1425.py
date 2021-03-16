# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-26 11:25
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models
from django.utils.text import slugify


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0038_auto_20180212_1556'),
    ]

    # Add slug first as a nullable, then create a slug value from the name, then
    # alter the slug field to be non-nullable.
    # See https://stackoverflow.com/questions/29787853/django-migrations-add-field-with-default-as-function-of-model
    def slug_from_name(apps, schema_editor):
        usertag = apps.get_model('course', 'UserTag')
        for tag in usertag.objects.all().iterator():
            tag.slug = slugify(tag.name)
            tag.save()

    operations = [
        migrations.AddField(
            model_name='usertag',
            name='slug',
            field=models.SlugField(null=True, help_text='Slug key for tag. If left blank, one is created from name', max_length=20),
            preserve_default=False,
        ),
        migrations.RunPython(slug_from_name),
        migrations.AlterField(
            model_name='usertag',
            name='slug',
            field=models.SlugField(help_text='Slug key for tag. If left blank, one is created from name', max_length=20),
        ),
        migrations.AlterField(
            model_name='usertag',
            name='color',
            field=colorfield.fields.ColorField(default='#CD0000', help_text='Color that is used as background for this tag', max_length=10),
        ),
        migrations.AlterField(
            model_name='usertag',
            name='description',
            field=models.CharField(blank=True, help_text='Describe the usage or meaning of this tag', max_length=155),
        ),
        migrations.AlterField(
            model_name='usertag',
            name='name',
            field=models.CharField(help_text='Display name for tag', max_length=20),
        ),
    ]
