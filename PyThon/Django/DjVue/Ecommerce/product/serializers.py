from product.models import Product, ProductPhoto
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = ('name', 'price', 'description', 'amount','photos')
        fields = '__all__'


class ProductPhotoSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = ProductPhoto
        fields = '__all__'

 