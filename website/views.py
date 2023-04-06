from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Course, Module, Video, Comment, SubComment, Notes,Monitor, Tags, Quiz, Question, Answer
from user.models import Profile, Student, Organization, Teacher
from datetime import datetime, timedelta


# Create your views here.

def index(request):
    courses = Course.objects.all().values()
    context = {
        "courses": courses
    }
    return render(request, 'website/home.html', context)

def contact(request):
    
    return render(request, 'website/contact.html')

def courseviewpage(request):
    return render(request,'website/courseviewpage.html')    

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        profile=Profile.objects.filter(user=request.user)
       
        if profile.exists():
            profile=Profile.objects.get(user=request.user)
            context={
            "profile": profile
            }
            return render(request, 'website/dashboard.html', context)
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
                
            course=Course()
            course.name=name
            course.description=description
            course.image_course=image_course
            course.price=price
            course.small_description=small_description
            course.learned=learned
            course.teacher = teacher
            course.organization = teacher.organization
            course.created_at=datetime.today()
            course.updated_at=datetime.today()
            course.save()
            
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
    course = get_object_or_404(Course, id=course_id)
    if(course.teacher.profile == request.user.profile):
        course = get_object_or_404(Course, pk=course_id)
        if request.method == 'POST':
            course.delete()
            return redirect('index')
        return render(request, 'website/delete_course.html', {'course': course})
    else:
        return redirect('course_detail', course_id=course.id)

def course(request):
    teacher=get_object_or_404(Teacher,profile=request.user.profile)
    courses=Course.objects.filter(teacher=teacher)
    context={
        "courses":courses,
    }
    return render(request,'website/courses.html', context)



def create_module(request, course_id):
    course = Course.objects.get(id=course_id)
    course.total_module += 1

    if request.method == 'POST':
        module_name = request.POST['module_name']
        module_number = course.total_module
        module=Module()
        module.name = module_name
        module.course=course
        module.number = module_number
        module.save()
        number=0
        for video in request.FILES.getlist('video'):
            video_name = video.name.split('.')[0]
            number += 1
            Video.objects.create(module=module, video=video, name=video_name, course=course, number=number)

        for note in request.POST.getlist('notes[]'):
            if note.strip():
                module.total_notes += 1
                Notes.objects.create(user=request.user, module=module, description=note, number=module.total_notes)

        return redirect('course_modules', course_id=course_id)

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

        return redirect('course_modules', course_id=course_id)

    return render(request, 'website/update_module.html', {'course': course, 'module': module})


def delete_module(request, course_id, module_id):
    course = Course.objects.get(id=course_id)
    module = Module.objects.get(id=module_id)

    if request.method == 'POST':
        module.delete()
        return redirect('course_modules', course_id=course_id)

    return render(request, 'website/delete_module.html', {'course': course, 'module': module})



def course_modules(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    modules = Module.objects.filter(course=course)
    context = {
        'course': course,
        'modules': modules,
    }
    return render(request, 'website/course_module_details.html', context=context)


def quiz_list(request, video_id):
    quizzes = Quiz.objects.filter(video=video_id)
    return render(request, 'website/quiz_list.html', {'quizzes': quizzes})


def view_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    return render(request, 'website/view_quiz.html', {'quiz': quiz})

def create_quiz(request, video_id):
    video = Video.objects.get(id=video_id)
    if request.user.profile != video.module.course.teacher.profile:
        return HttpResponse('You do not have permission to access this page')
    if request.method == 'POST':
        pass_mark = request.POST.get('pass_mark')
        start_time_str = request.POST.get('timestamp')
        if start_time_str:
            start_time = timedelta(seconds=float(start_time_str))
        else:
            start_time = timedelta(seconds=0)

        quiz = Quiz.objects.create(
            video=video,
            start_time=start_time,
            pass_mark=pass_mark,
        )

        question_text = request.POST.get('question_text')
        question = Question.objects.create(
            quiz=quiz,
            text=question_text,
        )

        answer1_text = request.POST.get('answer1_text')
        answer1_is_correct = request.POST.get('answer1_is_correct') == 'on'
        answer1 = Answer.objects.create(
            question=question,
            text=answer1_text,
            is_correct=answer1_is_correct,
        )

        answer2_text = request.POST.get('answer2_text')
        answer2_is_correct = request.POST.get('answer2_is_correct') == 'on'
        answer2 = Answer.objects.create(
            question=question,
            text=answer2_text,
            is_correct=answer2_is_correct,
        )

        answer3_text = request.POST.get('answer3_text')
        answer3_is_correct = request.POST.get('answer3_is_correct') == 'on'
        answer3 = Answer.objects.create(
            question=question,
            text=answer3_text,
            is_correct=answer3_is_correct,
        )

        answer4_text = request.POST.get('answer4_text')
        answer4_is_correct = request.POST.get('answer4_is_correct') == 'on'
        answer4 = Answer.objects.create(
            question=question,
            text=answer4_text,
            is_correct=answer4_is_correct,
        )
        return redirect('quiz_detail', quiz_id=quiz.id)

    return render(request, 'website/create_quiz.html', {'video': video})


def update_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)

    if request.method == 'POST':
        quiz.video_id = request.POST.get('video')
        quiz.start_time = request.POST.get('timestamp')
        quiz.pass_mark = request.POST.get('pass_mark')

        quiz.questions.all().delete()

        for i in range(1, 6):
            question_text = request.POST.get(f'question_{i}')
            if not question_text:
                continue

            question = Question.objects.create(quiz=quiz, text=question_text)

            answer1_text = request.POST.get(f'question_{i}_answer_1')
            answer1_correct = request.POST.get(f'question_{i}_answer_1_correct') == 'on'
            Answer.objects.create(question=question, text=answer1_text, is_correct=answer1_correct)

            answer2_text = request.POST.get(f'question_{i}_answer_2')
            answer2_correct = request.POST.get(f'question_{i}_answer_2_correct') == 'on'
            Answer.objects.create(question=question, text=answer2_text, is_correct=answer2_correct)

            answer3_text = request.POST.get(f'question_{i}_answer_3')
            answer3_correct = request.POST.get(f'question_{i}_answer_3_correct') == 'on'
            Answer.objects.create(question=question, text=answer3_text, is_correct=answer3_correct)

            answer4_text = request.POST.get(f'question_{i}_answer_4')
            answer4_correct = request.POST.get(f'question_{i}_answer_4_correct') == 'on'
            Answer.objects.create(question=question, text=answer4_text, is_correct=answer4_correct)

        quiz.save()

        return redirect('quiz-detail', quiz_id=quiz.id)

    return render(request, 'quiz/update_quiz.html', {'quiz': quiz})


def delete_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    if request.method == 'POST':
        quiz.delete()
        return redirect('quiz_list')
    return render(request, 'website/delete_quiz.html', {'quiz': quiz})



def make_teacher(request):
    r_profile=get_object_or_404(Profile, user=request.user)
    organization=Organization.objects.filter(profile=r_profile)
    if organization.exists():
        organization=Organization.objects.get(profile=r_profile)
        profiles = Profile.objects.all()
        context = {
            'profiles': profiles
        }
        
        if request.method == 'POST':
            profile_id=request.POST.get('profile_id')
            r_profile=get_object_or_404(Profile, id=profile_id)
            r_profile.status="Teacher"
            r_profile.save()
            teacher=Teacher.objects.create(profile=r_profile, organization=organization)
            student=get_object_or_404(Student,profile=r_profile)
            student.delete()
            teacher.save()
            return redirect('make_teacher')                           
        return render(request, 'website/make_teacher.html', context)
    else:
        return redirect('index')

def teacher_list(request):
    r_profile = get_object_or_404(Profile, user=request.user)
    organization = Organization.objects.filter(profile=r_profile)
    if organization.exists():
        organization = Organization.objects.get(profile=r_profile)
        teachers = Teacher.objects.filter(organization=organization)
        profiles = [teacher.profile for teacher in teachers]
        context = {'profiles': profiles}
        return render(request, 'website/teacher_list.html', context)
    else:
        return redirect('index')


def allcourses(request):
    courses = Course.objects.all().values()
    context = {
        "courses": courses
    }
    return render(request, 'website/allcourses.html', context)