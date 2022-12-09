from django.contrib import admin

from .models import AvaliableDetail, DetailsType


@admin.register(DetailsType)
class DetailsTypeAdmin(admin.ModelAdmin):
    list_display = ['type']


@admin.register(AvaliableDetail)
class AvailableDetailAdmin(admin.ModelAdmin):
    list_display = ['type', 'name']
