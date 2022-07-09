from django.shortcuts import redirect, render
from music.models import *

# Create your views here.
def AddAlbum(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            detail = request.POST.get('detail') 
            star = request.POST.get('star')
            logo = request.POST.get('logo')
            if title ==  '' or star == '' or logo == '':
                return render(request,'music/add_album.html')
            else:
                new_album = Album()
                new_album.title = title
                new_album.detail = detail
                new_album.star = star
                new_album.logo = logo
                new_album.user = request.user
                new_album.save()
                return redirect('homepage:index')
        
        return render(request,'music/add_album.html')
    else:
        return redirect('homepage:login')

def DeleteAlbum(request,id):
    if request.user.is_authenticated:        
        get_album = Album.objects.get(albumId=id)
        get_album.delete() 
        return redirect('homepage:index')
    else:
        return redirect('homepage:login')

def EditAlbum(request,id):
    if request.user.is_authenticated:    
        get_album = Album.objects.get(albumId=id)   
        if request.method == 'POST':
            title = request.POST.get('title') 
            detail = request.POST.get('detail') 
            star = request.POST.get('star')
            logo = request.POST.get('logo')
            get_album.title = title
            get_album.detail = detail
            get_album.star = star
            get_album.logo = logo
            get_album.save()
            return redirect('homepage:index')          
        context ={
            'album':get_album,
        }
        
        return render(request,'music/edit_album.html',context)
    else:
        return redirect('homepage:login')       
