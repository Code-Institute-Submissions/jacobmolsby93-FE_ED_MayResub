# Generated by Django 3.2.8 on 2022-03-24 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment_user',
        ),
    ]
