# Generated by Django 4.1.7 on 2023-03-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_subscribe_alter_comments_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]