# Generated by Django 3.2 on 2022-06-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_auto_20220620_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='cilent',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
