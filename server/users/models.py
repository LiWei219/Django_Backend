from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Operator(models.Model):
    uesr=models.OneToOneField(User)
    privilege = models.IntegerField()

class Administrator(models.Model):
    uesr=models.OneToOneField(User)
    privilege = models.IntegerField()

class Researcher(models.Model):
    uesr=models.OneToOneField(User)
    privilege = models.IntegerField()

    def __unicode__(self):
        return self.username

