# Generated by Django 3.2.8 on 2022-04-01 23:24

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_bloguser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile-image'),
        ),
    ]
