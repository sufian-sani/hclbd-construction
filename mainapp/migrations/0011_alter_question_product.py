# Generated by Django 3.2 on 2022-06-19 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_question_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='mainapp.product'),
        ),
    ]