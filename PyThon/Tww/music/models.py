from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Tạo album
class Album(models.Model):
    albumId = models.AutoField(primary_key=True)
    title = models.CharField(max_length  = 250, blank = True, null = True)
    detail = models.CharField(max_length  = 1000, blank = True, null = True)
    logo = models.CharField(max_length = 250, blank = True, null = True)
    star = models.CharField(max_length = 250, blank = True, null = True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,blank = True, null = True)  # Người tạo Album

    def __str__(self):
        return self.title

class Song(models.Model):
    songId = models.AutoField(primary_key = True)
    albumId = models.ForeignKey(Album,on_delete=models.DO_NOTHING, blank = True, null = True)
    songName = models.CharField(max_length = 250, blank = True, null = True)
    audio =  models.CharField(max_length = 250, blank = True, null = True)
    star = models.CharField(max_length = 250, blank = True, null = True)
