# Generated by Django 4.0.3 on 2022-04-21 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0009_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='coding', max_length=255, unique=True),
        ),
    ]