from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    sid = models.IntegerField()
    saddress =  models.CharField(max_length=20)
    trainedby = models.CharField(max_length=20)

    class Meta:
        db_table = 'restapp12_tbl_student'

