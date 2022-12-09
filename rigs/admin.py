from django.contrib import admin
from .models import AvaliableDetail
from .models import DetailsType



# Register your models here.
@admin.register(DetailsType)
class DetailsTypeAdmin(admin.ModelAdmin):
    list_display = ["type"]
    

@admin.register(AvaliableDetail)
class AvaliableDetailAdmin(admin.ModelAdmin):
    list_display = ("type","name")