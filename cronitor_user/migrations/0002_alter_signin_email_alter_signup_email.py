# Generated by Django 4.0.3 on 2022-03-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cronitor_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]