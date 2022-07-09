from django.db import models


# Create your models here.
class UpForm(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField()
    body = models.TextField()

    def __str__(self):
        return self.title
