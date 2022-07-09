from django.urls.conf import path
from . import views

app_name  = 'homepage'

urlpatterns = [
    path('', views.index,  name= 'index'),  # tạo đường dẫn  đến hàm login trong view.py
    path('login', views.MyLogin,  name=  'login'),  # tạo đường dẫn  đến hàm login trong view.py
    path('logout', views.MyLogout, name = 'logout'),
    path('register', views.MyRegister, name = 'register'),
]
