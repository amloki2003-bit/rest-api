from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=20)
    address =  models.CharField(max_length=20)
    mail = models.EmailField(max_length=30)
    age = models.IntegerField()

    class Meta:
        db_table = 'restapp11_tbl_manager'

    @receiver(post_save,sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender,instance=None,created = False,**kwargs):
        if created:
            Token.objects.create(user=instance)