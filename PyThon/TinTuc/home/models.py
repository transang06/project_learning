from django.db import models


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    ten = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    noidung = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten
