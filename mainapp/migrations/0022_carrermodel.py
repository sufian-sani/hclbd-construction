# Generated by Django 3.2 on 2022-06-19 19:39

import autoslug.fields
import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_supplyhistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarrerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('salary', models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('post_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
            ],
        ),
    ]