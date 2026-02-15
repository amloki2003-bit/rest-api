from django.contrib import admin
from restapp13.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','address','mail','age']
