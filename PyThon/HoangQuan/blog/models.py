from django.db import models


# Create your models here.
class postForm(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title