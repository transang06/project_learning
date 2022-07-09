from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class MyUser(AbstractUser):
    avatar = models.FileField(blank=True, null=True)
    namSinh = models.DateField(blank=True, null=True)
    gioiTinh = models.CharField(max_length=100, blank=True, null=True)


class Follower(models.Model):
    f_id = models.AutoField(primary_key=True)
    main_user = models.ForeignKey(MyUser(id), related_name='main_user', on_delete=models.CASCADE, null=False)
    user_fl = models.ForeignKey(MyUser(id), related_name='user_fl', on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    post = models.AutoField(primary_key=True)
    user = models.ForeignKey(MyUser(id), on_delete=models.CASCADE, blank=True, null=False)
    content = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    comment = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(MyUser(id), on_delete=models.CASCADE, blank=False, null=False)
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Tim(models.Model):
    tim_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=False, null=False)
    user = models.ForeignKey(MyUser(id), on_delete=models.CASCADE, blank=False, null=False)
