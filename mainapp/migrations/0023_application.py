# Generated by Django 3.2 on 2022-06-19 20:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_carrermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.CharField(max_length=3)),
                ('job_title', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801711111000'.", regex='^\\+?1?\\d{11,14}$')])),
                ('email', models.EmailField(max_length=254)),
                ('expected_salary', models.CharField(blank=True, max_length=7, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('resume', models.FileField(upload_to='resume/cv')),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Job Application',
                'verbose_name_plural': 'Job Applications',
            },
        ),
    ]
