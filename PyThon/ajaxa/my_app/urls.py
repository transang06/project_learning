from django.urls import path
from my_app.views import (
    indexView,
    postFriend, checkNickName, FriendView,
)

urlpatterns = [
    # ... other urls
    path('', indexView),
    path('post/ajax/friend', postFriend, name = "post_friend"),
    path('get/ajax/validate/nickname', checkNickName, name="validate_nickname"),
    path("", FriendView.as_view(), name="friend_cbv"),

    # ...
]