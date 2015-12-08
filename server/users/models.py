from django.db import models

# Create your models here.
class User(models.Model):
    UserID = models.CharField(max_length = 100)
    Password = models.CharField(max_length = 100)
    UserGroup = models.IntegerField()
    Email = models.CharField(max_length = 100)
    Url = models.URLField()
