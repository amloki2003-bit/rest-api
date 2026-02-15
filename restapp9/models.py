from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    mail = models.CharField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = 'restapp9_tbl_customer'