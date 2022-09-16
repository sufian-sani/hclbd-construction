# Generated by Django 3.2 on 2022-06-20 07:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0025_cilent_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=14, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+8801711111000'.", regex='^\\+?1?\\d{11,14}$')])),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Request Quote',
                'verbose_name_plural': 'Request Quote',
            },
        ),
    ]