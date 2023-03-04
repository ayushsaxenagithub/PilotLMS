from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Course, Module, Video, Comment, SubComment, Notes,Monitor, Tags
from user.models import Profile, Student, Organization, Teacher

# Create your views here.

def index(request):
    return render(request, 'main/base.html')



@login_required
def create_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        organisation_id = request.POST.get('organisation')
        teacher_ids = request.POST.getlist('teacher')
        student_ids = request.POST.getlist('student')
        tag_ids = request.POST.getlist('tag')
        description = request.POST.get('description')
        image_course = request.FILES.get('image_course')
        price = request.POST.get('price')
        small_description = request.POST.get('small_description')
        learned = request.POST.get('learned')

        course = Course.objects.create(
            name=name,
            organisation_id=organisation_id,
            description=description,
            image_course=image_course,
            price=price,
            small_description=small_description,
            learned=learned,
        )

        course.teacher.set(teacher_ids)
        course.students.set(student_ids)
        course.tags.set(tag_ids)

        return redirect('course_detail', course_id=course.id)

    organisations = Organization.objects.all()
    teachers = Teacher.objects.all()
    students = Student.objects.all()
    tags = Tags.objects.all()

    context = {
        'organisations': organisations,
        'teachers': teachers,
        'students': students,
        'tags': tags,
    }

    return render(request, 'website/create_course.html', context)

@login_required
def course_detail(request, course_id):
    course = Course.objects.get(id=course_id)

    context = {
        'course': course,
    }

    return render(request, 'website/course_detail.html', context)


