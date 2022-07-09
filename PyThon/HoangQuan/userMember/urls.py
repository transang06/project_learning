from django.urls import path
from . import views
app_name = 'userMember'
urlpatterns = [
    path('register/',views.registerUser.as_view(), name='register' ),
    path('login/',views.loginUser.as_view(), name='login' ),
    path('logout/',views.logoutUser, name='logout' ),
    path('', views.privatePage.as_view(), name='privatePage'),

]
