# Generated by Django 2.1.7 on 2019-03-01 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_lessoncourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='url_video',
        ),
    ]
