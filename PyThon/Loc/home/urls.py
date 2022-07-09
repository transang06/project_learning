from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('login/', views.Login_user.as_view(), name='login'),
    path('register/', views.Register_user.as_view(), name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('newpost/', views.DangBai.as_view(), name='newpost'),
    path('profile/<str:username>', views.Profile.as_view(), name='profile'),
    path('search/', views.Search.as_view(), name='search'),
    path('edit_profile/', views.Edit_profile.as_view(), name='edit_profile'),
    path('comments/<int:post_id>', views.comment_post, name='comments'),

]
