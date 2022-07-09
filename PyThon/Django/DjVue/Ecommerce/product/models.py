from django.db import models

# Create your models here.

class ProductPhoto(models.Model):
    url = models.FileField(upload_to='products',null=True)    
    created_at = models.DateTimeField(auto_now_add=True)
    def _str_(self):
        return self.url
    
class Product(models.Model):
    name = models.CharField(max_length=555)
    price = models.FloatField(default=0)
    description = models.TextField()
    amount = models.IntegerField(default=0)
    photos = models.ManyToManyField(ProductPhoto)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name