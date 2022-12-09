from django.db import models


class User(models.Model):
    login = models.CharField(unique=True, max_length=50)
    nickname = models.CharField(unique=False, max_length=50, default='samplenickname')

    password = models.TextField()

    user_email = models.EmailField(unique=True, max_length=254)
    email_verified = models.BooleanField(default=False)

    phone_number = models.TextField(
        unique=True,
    )
    phone_number_verified = models.BooleanField(default=False)

    user_avatar = models.TextField(
        default="https://cdn-icons-png.flaticon.com/512/1160/1160040.png?w=360"
    )

    clan_id = models.IntegerField(default=-1)
    client_fio = models.CharField(max_length=128)

    profile_description = models.TextField(default="Profile description not provided")


class Token(models.Model):
    token = models.TextField()
    user_id = models.IntegerField(default=-1)


class EmailVerificationCode(models.Model):
    code = models.IntegerField(default=000000)
    email = models.EmailField(unique=False, max_length=254)
    used = models.BooleanField(default=False)
    token = models.TextField(unique=True)
