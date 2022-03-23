# Generated by Django 3.2.8 on 2022-03-23 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_auto_20220323_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('post_title', models.CharField(max_length=254)),
                ('post_body', models.TextField()),
                ('posted', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_author', to='users.bloguser')),
                ('likes', models.ManyToManyField(blank=True, related_name='blog_likes', to='users.BlogUser')),
            ],
            options={
                'ordering': ['-posted'],
            },
        ),
    ]