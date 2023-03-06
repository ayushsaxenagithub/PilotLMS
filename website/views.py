from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Course, Module, Video, Comment, SubComment, Notes,Monitor, Tags
from user.models import Profile, Student, Organization, Teacher

# Create your views here.

def index(request):
    return render(request, 'website/home.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        profile=Profile.objects.filter(user=request.user)
        if profile.exists():
            return render(request, 'website/dashboard.html')
        else:
            return HttpResponse('Something went wrong')



def create_course(request):
    if request.user.profile.status == 'Teacher':
        if request.method == 'POST':
            name = request.POST.get('name')
            description = request.POST.get('description')
            image_course = request.FILES.get('image_course')
            price = request.POST.get('price')
            small_description = request.POST.get('small_description')
            learned = request.POST.get('learned')


            tags_input = request.POST.get('tags')
            tags_list = [tag.strip() for tag in tags_input.split(',') if tag.strip()]

            tags = []
            for tag_name in tags_list:
                tag, created = Tags.objects.get_or_create(name=tag_name)
                tags.append(tag)
            teacher=Teacher.objects.get(profile=request.user.profile)
                

            course = Course.objects.create(
                name=name,
                description=description,
                image_course=image_course,
                price=price,
                small_description=small_description,
                learned=learned,
                modules=0,
                teacher = teacher,
                organization = teacher.organization,
                created_at=datetime.today(),
                updated_at=datetime.today(),
            )
            course.tags.set(tags)

            return redirect('course_detail', course_id=course.id)

        return render(request, 'website/create_course.html')
    else:
        return redirect('index')


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'website/course_detail.html', {'course': course})



def update_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    if(course.teacher.profile == request.user.profile):
        if request.method == 'POST':
            course.name = request.POST.get('name')
            course.description = request.POST.get('description')
            course.price = request.POST.get('price')
            course.small_description = request.POST.get('small_description')
            course.learned = request.POST.get('learned')
            tags = request.POST.get('tags').split(',')
            course.update_at = datetime.today()

            for tag in tags:
                tag = tag.strip()
                if tag:
                    obj, created = Tags.objects.get_or_create(name=tag)
                    course.tags.add(obj)
            course.save()
            return redirect('course_detail', course_id=course.id)
        return render(request, 'website/update_course.html', {'course': course})
    else:
        return redirect('course_detail', course_id=course.id)



def delete_course(request, course_id):
    if(course.teacher.profile == request.user.profile):
        course = get_object_or_404(Course, pk=course_id)
        if request.method == 'POST':
            course.delete()
            return redirect('index')
        return render(request, 'website/delete_course.html', {'course': course})
    else:
        return redirect('course_detail', course_id=course.id)

def create_module(request, course_id):
    course = Course.objects.get(id=course_id)
    course.modules+=1

    if request.method == 'POST':
        module_name = request.POST['module_name']
        module.number=course.modules
        module = Module.objects.create(course=course, name=module_name)

        for video in request.FILES.getlist('video'):
            video_name = video.name.split('.')[0]
            Video.objects.create(module=module, video=video, name=video_name, course=course)

        for note in request.POST.getlist('note'):
            Notes.objects.create(user=request.user, module=module, description=note)

        return redirect('course_detail', course_id=course_id)

    return render(request, 'website/create_module.html', {'course': course})


def update_module(request, course_id, module_id):
    course = Course.objects.get(id=course_id)
    module = Module.objects.get(id=module_id)

    if request.method == 'POST':
        module_name = request.POST['module_name']
        module.name = module_name
        module.save()

        videos_to_delete = request.POST.getlist('delete_video')
        for video_id in videos_to_delete:
            Video.objects.filter(id=video_id).delete()

        for video in request.FILES.getlist('video'):
            video_name = video.name.split('.')[0]
            Video.objects.create(module=module, video=video, name=video_name, course=course)

        notes_to_delete = request.POST.getlist('delete_note')
        for note_id in notes_to_delete:
            Notes.objects.filter(id=note_id).delete()

        for note in request.POST.getlist('note'):
            Notes.objects.create(user=request.user, module=module, description=note)

        return redirect('course_detail', course_id=course_id)

    return render(request, 'website/update_module.html', {'course': course, 'module': module})


def delete_module(request, course_id, module_id):
    course = Course.objects.get(id=course_id)
    module = Module.objects.get(id=module_id)

    if request.method == 'POST':
        module.delete()
        return redirect('course_detail', course_id=course_id)

    return render(request, 'website/delete_module.html', {'course': course, 'module': module})



def course_modules(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = course.module_set.all()
    context = {
        'course': course,
        'modules': modules,
    }
    return render(request, 'website/course_module_details.html', context=context)



