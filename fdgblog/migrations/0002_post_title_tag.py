# Generated by Django 5.1 on 2024-08-08 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fdgblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='a fdgblog title', max_length=255),
        ),
    ]
