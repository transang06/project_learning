from django.db import models


# Create your models here.
class ContactForm(models.Model):
    username = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.email
