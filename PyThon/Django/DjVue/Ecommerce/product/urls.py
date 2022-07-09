from django.conf.urls import include
from django.urls import path
from product import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'product')
router.register(r'photo', views.PhototView, 'photo')


app_name = 'product'
urlpatterns = [
    path('', include(router.urls)),
    path('photo/<int:id>', views.ProductPhototView.as_view(),name="productPhoto"),
    path('detail/<int:id>', views.Detail.as_view(),name="Detail")
    
]
