from django.db import models

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)
    mail = models.CharField(max_length=30)
    age  = models.IntegerField()

    class Meta:
        db_table = 'restapp6_tbl_manager'