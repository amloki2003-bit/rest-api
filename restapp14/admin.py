from django.contrib import admin
from restapp14.models import Student

# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','sid','saddress','mail','age']