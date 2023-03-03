from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages





# messages.error(request,'User not found')
# @login_required(login_url='login')
def profile(request):
    user = Profile.objects.all()
    context ={'user': user}
    return render(request,'user/profiles.html',context)

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        # return redirect('profile')
        return redirect('index')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(username=email)
        except:
            messages.error(request,'User not found')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrect')
    return render(request,'index.html',)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page='signup'
    if (user.is_authenticated):
        pass
    else:
        if request.method == 'POST':
            username = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pwd = request.POST.get('password')
            cnfrm_pwd = request.POST.get('confirmpassword')
            try:
                if pwd == cnfrm_pwd:
                    profile=Profile.objects.filter(email=email)
                    user=User.objects.filter(email=email)

                    if not user.exists():
                        user=User.objects.create_user(username=email,email=email)
                        user.set_password(pwd)
                        profile=Profile.objects.create(user=user,name=username,email=email,phone=phone)
                        user.save()
                        profile.save()
                        return render(request, 'index.html')
                    else:
                        return render(request, 'index.html',{"msg": "User already exists"})
                else:
                    return render(request, 'index.html',{ "msg":"Confirm Password is not equal to Password" }) 
                   
            except Exception as e:
                return HttpResponse(e)    





