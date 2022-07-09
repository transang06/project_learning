from django.contrib import admin

# Register your models here.
from home.models import *

admin.site.register(MyUser)
admin.site.register(Follower)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tim)
