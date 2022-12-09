from django.contrib import admin

from users.models import User
from users.models import Token
from users.models import EmailVerificationCode

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id","login","user_email","phone_number","client_fio","clan_id")


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ("user_id","token")
    

@admin.register(EmailVerificationCode)
class EmailVerificationCodeAdmin(admin.ModelAdmin):
    list_display = ("email","code","used","token")
    
