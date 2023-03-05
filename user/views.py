from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
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


def update_profile(request):
    print(request.user)
    if request.user.is_authenticated:
        
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
            date_of_birth = request.POST.get('date_of_birth')
            location=request.POST.get('location')
            website = request.POST.get('website')
            founded_year = request.POST.get('founded_year')
            employees = request.POST.get('employees')
            department = request.POST.get('department')
            profile = request.POST.get('profile')
            organization = request.POST.get('organization')
            qualification = request.POST.get('qualification')
            bio = request.POST.get('bio')
            date_of_birth = request.POST.get('date_of_birth')
            date_of_birth = request.POST.get('date_of_birth')
            research_interests = request.POST.get('research_interests')

            try:
                r_profile = Profile.objects.get(user=request.user)
            except Profile.DoesNotExist:
                raise ValueError("Profile does not exist for user")
            r_profile.name=name    
            r_profile.image_profile=image_profile
            r_profile.shortBio=shortBio
            r_profile.github=github
            r_profile.youtube=youtube
            r_profile.twitter=twitter
            r_profile.facebook=facebook
            r_profile.instagram=instagram
            r_profile.linkedin=linkedin

            r_profile.save()
            if(r_profile.status=="Student"):
                student = Student.objects.filter(profile=r_profile)
                if student.exists():
                    student=Student.objects.get(profile=r_profile)
                else:
                    student=Student()  
                
                student.profile = r_profile
                student.department = department
                if(date_of_birth is not None ):
                    student.date_of_birth = date_of_birth
                student.save()
                return redirect('index')    
            elif(r_profile.status=="Teacher"):
                teacher = Teacher.objects.filter(profile=r_profile)
                if teacher.exists():
                    teacher=Teacher.objects.get(profile=r_profile)
                else:
                    teacher=Teacher()  
                 
                teacher.profile = r_profile
                teacher.department = department
                teacher.organization = organization
                teacher.qualification = qualification
                teacher.bio = bio
                teacher.research_interests = research_interests

                if(date_of_birth is not None ):
                    teacher.date_of_birth = date_of_birth
                teacher.save()
                return redirect('index') 
            elif(r_profile.status=="Organization"):
                organization = Organization.objects.filter(profile=r_profile)
                if organization.exists():
                    organization=Organization.objects.get(profile=r_profile)
                else:
                    organization=Organization()  
                organization.profile = r_profile
                organization.department = department
                organization.location = location
                organization.website = website
                organization.founded_year = founded_year
                organization.employees = employees

                if(founded_year is not None ):
                    organization.founded_year = founded_year
                organization.save()
                return redirect('index') 
            else:
                return HttpResponse("Something went wrong")
            student=Student.objects.filter(profile=r_profile)
            
            

        return render(request, 'user/update_profile.html')
    else:
        return redirect('index')














def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)
    
    if profile.status == 'Organization':
        organization = get_object_or_404(Organization, profile=profile)
        context = {'organization': organization}
    
    elif profile.status == 'Teacher':
        teacher = get_object_or_404(Teacher, profile=profile)
        context = {'teacher': teacher}
    
    else:
        student = get_object_or_404(Student, profile=profile)
        context = {'student': student}
    return render(request, 'user/user_detail.html', context)    