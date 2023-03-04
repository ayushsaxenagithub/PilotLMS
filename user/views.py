from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.contrib import messages
from .models import Teacher, Student, Organization





# messages.error(request,'User not found')
# @login_required(login_url='login')

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
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
            return redirect('index')
        else:
            messages.error(request,'Username or password is incorrect')
    return render(request,'user/login.html',)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page='signup'
    if (request.user.is_authenticated):
        return redirect('index')
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
                        return redirect('index')
                    else:
                        return render(request, 'user/register.html',{"msg": "User already exists"})
                else:
                    return render(request, 'user/register.html',{ "msg":"Confirm Password is not equal to Password" }) 
                   
            except Exception as e:
                return HttpResponse(e)
        return render(request, 'user/register.html')        


def create_profile(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        status = profile.status
        if request.method == 'POST':
            name = request.POST.get('name')
            image_profile = request.FILES.get('image_profile')
            shortBio = request.POST.get('shortBio')
            detail = request.POST.get('detail')
            github = request.POST.get('github')
            youtube = request.POST.get('youtube')
            twitter = request.POST.get('twitter')
            facebook = request.POST.get('facebook')
            instagram = request.POST.get('instagram')
            linkedin = request.POST.get('linkedin')
            department = request.POST.get('department')
            date_of_birth = request.POST.get('date_of_birth')

            student = Student()
            student.profile = profile
            profile=Profile.objects.create(
            user=request.user,    
            name=name,    
            image_profile=image_profile,
            shortBio=shortBio,
            detail=detail,
            github=github,
            youtube=youtube,
            twitter=twitter,
            facebook=facebook,
            instagram=instagram,
            linkedin=linkedin,
            )
            student=Student.objects.create(
                profile=profile,
                department=department,
                date_of_birth=date_of_birth,
            )
            return redirect('index')

        return render(request, 'user/create_profile.html')
    else:
        return redirect('index')


