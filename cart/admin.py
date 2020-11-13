from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(cartinfo)
class cartinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'ap', 'count']
