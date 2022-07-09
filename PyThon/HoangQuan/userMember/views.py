from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User


# Create your views here.
class registerUser(View):
    def get(self, request):
        rF = registerForm
        return render(request, 'userMember/register.html', {'rF': rF})

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create(username=username, email=email, password=password)
        user.save()
        return HttpResponse('đăng ki thành cong')


class loginUser(View):
    def get(self, request):
        lF = loginForm
        return render(request, 'userMember/login.html', {'lF': lF})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(request, username=User.objects.get(email=username), password=password)
        except:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'userMember/private.html')

        else:
            return HttpResponse('thaats baai')


def logoutUser(request):
    logout(request)
    return redirect('userMember:login')


# @login_required(login_url='/user/login/')
class privatePage(LoginRequiredMixin, View):
    login_url = '/user/login/'

    def get(self, request):
        return render(request, 'userMember/private.html')
