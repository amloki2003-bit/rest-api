from django.contrib import admin
from restapp12.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','sid','saddress','trainedby']
