# Generated by Django 4.1.3 on 2022-12-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_second_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='second_score',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
