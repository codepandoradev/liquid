# Generated by Django 3.2.2 on 2022-07-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220428_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
            ),
        ),
    ]
