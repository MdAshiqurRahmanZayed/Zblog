# Generated by Django 4.0.3 on 2022-04-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0013_post_snippet_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click link above to read the blog post', max_length=255),
        ),
    ]
