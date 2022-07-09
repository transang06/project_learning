from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from music.models import Album


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        albums = Album.objects.filter(user=request.user)
        user= request.user        
        context = {
            'albums': albums,
            'user': user
        }
        return render(request,'homepage/index.html',context)
    else:
        return redirect('homepage:login')




def MyLogin(request):
    if request.user.is_authenticated:
        return redirect('homepage:index')
    else:
        if request.method == 'POST':
            # Lấy username và password 
            username = request.POST.get('username')
            password = request.POST.get('password')
            # kiểm tra xem username và password có trong dữ liệu hay không
            user = authenticate(username = username, password = password)
            if user is not None: # Nếu tìm thấy user có userName và password đã nhập
                if user.is_active:  #  Tài khoản có bị vô hiệu hóa hay không
                    login(request,user)
                    # trả  về trang index
                    # Lấy tất cả album của user đã đăng nhập
                    albums = Album.objects.filter(user=request.user)
                    return render(request,'homepage/index.html',{'albums':albums})
                else:
                    return render(request,'homepage/login.html',{'message':'Tài khoản đã bị vô hiệu hóa'})
            else:
                return render(request,'homepage/login.html',{'message':'Tài khoản không tồn tại'})
        return render(request,'homepage/login.html')
    

def MyLogout(request):
    # nếu không có tài khoản nào thì không thực hiện đăng xuất
    try:
        logout(request)
    except:
        pass
    # nếu đăng xuất thành công thì trả về trang đăng nhập
    return redirect('homepage:login')

    
def MyRegister(request):
    # Nếu đã đăng nhập thì trả về index
    if request.user.is_authenticated:
        return redirect('homepage:index')
    else:
        if request.method =='POST':
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            if username == '' or password1 == ''or password2 =='' or password1 != password2:
                return  render(request,'homepage/register.html',{'message':'Sai gì đó'})
            else:
                new_user = User()
                new_user.username  = username
                new_user.set_password(password1)
                new_user.save()
                user = authenticate(username = username, password = password1)
                login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('homepage:index')

    return render(request,'homepage/register.html')
