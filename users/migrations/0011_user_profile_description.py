# Generated by Django 4.1.3 on 2022-11-11 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_emailverificationcode_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_description',
            field=models.TextField(default='Profile description not provided'),
        ),
    ]
