from django.shortcuts import render

# Create your views here.
from django.views import View

from home.models import Post


class Index(View):
    def get(self, request):
        sql = "SELECT * From home_post ORDER BY post_id DESC "
        post = Post.objects.raw(sql)
        post2= post[:2]
        context = {
            'post': post,
            'post2': post2
        }
        return render(request, 'home/index.html', context)