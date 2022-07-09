from rest_framework.views import APIView
from product.models import Product, ProductPhoto
from product.serializers import ProductPhotoSerializer, ProductSerializer
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

# Create your views here.
class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

# class ProductPhototView(viewsets.ModelViewSet):
#     serializer_class = ProductPhotoSerializer
#     queryset = ProductPhoto.objects.filter(product=1)


class ProductPhototView(APIView):
    def get(self, request,id):
        photos = ProductPhoto.objects.filter(product=id)
     
        mydata = ProductPhotoSerializer(photos, many=True)
        return Response(data=mydata.data, status=status.HTTP_200_OK)

class Detail(APIView):
    def get(self, request,id):
        detail = Product.objects.get(id=id)
       
        mydata = ProductSerializer(detail)
        return Response(data=mydata.data, status=status.HTTP_200_OK)



class PhototView(viewsets.ModelViewSet):
    serializer_class = ProductPhotoSerializer
    queryset = ProductPhoto.objects.all()
