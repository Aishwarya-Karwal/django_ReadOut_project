# Generated by Django 4.1.7 on 2023-04-09 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_image_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='date',
        ),
    ]
