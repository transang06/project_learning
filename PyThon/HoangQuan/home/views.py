from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        name = request.POST['email']
        password =request.POST['password']

        User.objects.create()
