from django.contrib import admin
from restapp11.models import Manager

# Register your models here.

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ['name','address','mail','age']