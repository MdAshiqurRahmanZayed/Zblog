# Generated by Django 4.0.3 on 2022-04-17 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theBlog', '0005_post_upload_to'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='upload_to',
        ),
    ]