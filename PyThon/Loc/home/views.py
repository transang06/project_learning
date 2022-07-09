from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from home.models import MyUser, Post, Comment


class Index(View):
    def get(self, request):
        if request.user.is_authenticated:
            sql = "SELECT * FROM home_post a JOIN home_myuser b ON a.user_id = b.id ORDER BY created_at DESC "
            home_post = Post.objects.raw(sql)
            context = {
                'home_post': home_post
            }

            return render(request, 'home/feed.html', context)
        else:
            return redirect('home:login')

class Register_user(View):
    def get(self, request):
        return render(request, 'home/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password1 = request.POST.get('password1')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')
        if password != password1:
            return render(request, 'home/register.html', {'message': 'Mật khẩu không trùng nhau'})
        else:
            new_user = MyUser()
            new_user.username = username
            new_user.email = email
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.set_password(password)
            new_user.namSinh = birthday
            new_user.gioiTinh = gender
            new_user.save()
            newuser = MyUser.objects.filter(username=username)
            if newuser:
                return redirect('home:login')
            else:
                return render(request, 'home/register.html', {'message': 'Mật khẩu cần có cả chữ và sô'})


class Login_user(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home:index')
        else:
            return render(request, 'home/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:login')
            else:
                return render(request, 'home/login.html', {'message': 'Tài khoản đã bị vô hiệu hóa'})
        else:
            return render(request, 'home/login.html', {'message': 'Sai  tài khoản hoặc mật khẩu'})


def logout_user(request):
    try:
        logout(request)
    except:
        pass
    return redirect('home:login')


class DangBai(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'home/newpost.html')
        else:
            return redirect('home:login')

    def post(self, request):
        content = request.POST.get('content')
        photo = request.FILES['photo']
        get_user = MyUser.objects.get(id=request.user.id)
        newpost = Post()
        newpost.content = content
        newpost.photo = photo
        newpost.user = get_user
        newpost.save()
        return redirect('home:index')


class Profile(View):
    def get(self, request, username):
        if request.user.is_authenticated:
            sql_user = "SELECT * FROM home_myuser WHERE username ='" + str(username) + "'"
            user = MyUser.objects.raw(sql_user)
            sql_post = "SELECT * FROM home_post a JOIN home_myuser b ON a.user_id = b.id  WHERE username ='" + str(
                username) + "' ORDER BY created_at DESC "
            user_post = Post.objects.raw(sql_post)
            context = {
                'user_profile': user,
                'user_post': user_post
            }
            return render(request, 'home/profile.html', context)
        else:
            return redirect('home:login')


class Search(View):
    def post(self, request):
        if request.user.is_authenticated:
            key = request.POST.get('key')
            sqldc = " WHERE username like  '" + str(key) + "%' "
            sql_user = "SELECT * FROM home_myuser " + sqldc
            user = MyUser.objects.raw(sql_user)
            context = {
                'user_': user,
            }
            return render(request, 'home/explore.html', context)
        else:
            return redirect('home:login')


class Edit_profile(View):
    def get(self, request):
        if request.user.is_authenticated:
            sql_user = "SELECT * FROM home_myuser WHERE username ='" + str(request.user.username) + "'"
            user = MyUser.objects.raw(sql_user)
            context = {
                'user_profile': user,
            }
            return render(request, 'home/edit-profile.html', context)
        else:
            return redirect('home:login')

    def post(self, request):
        if request.user.is_authenticated:
            get_user = MyUser.objects.get(username=request.user.username)
            get_user.first_name = request.POST.get('first_name')
            get_user.last_name = request.POST.get('last_name')
            get_user.email = request.POST.get('email')
            get_user.namSinh = request.POST.get('namSinh')
            get_user.gioiTinh = request.POST.get('gender')
            try:
                get_user.avatar = request.FILES['avatar']
            except:
                pass
            get_user.save()
            sql_user = "SELECT * FROM home_myuser WHERE username ='" + str(request.user.username) + "'"
            user = MyUser.objects.raw(sql_user)
            context = {
                'user_profile': user,
                'mess': "Thành Công",
            }
            return render(request, 'home/edit-profile.html', context)
        else:
            return redirect('home:login')

def comment_post(request, post_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            content = request.POST.get('content')
            if content != '':
                new_cm = Comment()
                new_cm.content = content
                new_cm.user_id = request.user.id
                new_cm.post_id = post_id
                new_cm.save()

        sql_comments = "SELECT * FROM home_comment a JOIN home_myuser b ON  a.user_id = b.id WHERE a.post_id =" + str(
            post_id)
        post_comment = Post.objects.raw(sql_comments)
        context = {
            'post_comment': post_comment,
        }
        return render(request, 'home/ajax_cmt.html', context)

    else:
        return redirect('home:login')