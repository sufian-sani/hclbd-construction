# Generated by Django 3.2 on 2022-06-20 10:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_auto_20220620_1619'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='attribute_description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
