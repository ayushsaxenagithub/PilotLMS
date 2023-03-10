from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid
from django.utils import timezone
from user.models import Profile,Organization,Teacher,Student
from moviepy.editor import *

class Tags(models.Model):
    name=models.CharField(max_length=2000,blank=True, null=True)
    
class Course(models.Model):
    name = models.CharField(max_length=2000,blank=True,null=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null = True, blank = True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE, blank=True, null=True)
    enroller_user=models.ManyToManyField(User,blank=True, null=True, through="Enrollment")
    tags=models.ManyToManyField(Tags, blank=True, null=True)
    description=RichTextField(null=True, blank=True)
    image_course=models.ImageField(null=True, blank=True, default='blank_course.png',upload_to='course/')
    price = models.DecimalField(null=True, blank=True, default=0, max_digits=100, decimal_places=2)
    small_description = models.TextField(null=True, blank=True)
    learned = RichTextField(null = True, blank = True)
    created_at=models.DateTimeField(null=True, blank = True)
    updated_at=models.DateTimeField(null=True, blank =True)
    rating=models.FloatField(null=True, blank = True, default=0)
    total_video=models.IntegerField(null=True, blank = True)
    vidoes_time=models.CharField(max_length=2000,null=True, blank = True)
    total_module=models.IntegerField(blank=True, null=True, default=0)
    # def save(self, *args, **kwargs):
    #     self.total_video = Video.objects.filter(module=self).count()
    #     time = sum([video.duration for video in Video.objects.filter(module=self)])
    #     self.videos_time = str(timedelta(seconds=time))
    #     super().save(*args, **kwargs)
    def __str__(self):
        return self.name



class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name="enrollments",on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="user_courses", on_delete=models.CASCADE)
    class Meta:
        unique_together = ('course', 'student')


class Module(models.Model):
    name = models.CharField(max_length=2000, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    number = models.IntegerField(null=True, blank=True)    
    description = RichTextField(null=True, blank=True)
    total_video = models.IntegerField(null=True, blank=True, default=0)
    total_notes = models.IntegerField(null=True, blank=True, default=0)
    duration = models.CharField(max_length=2000, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.total_video = Video.objects.filter(module=self).count()
        time = sum([video.duration for video in Video.objects.filter(module=self)])
        self.duration = str(timedelta(seconds=time))
        super().save(*args, **kwargs)

class Video(models.Model):
    name = models.CharField(max_length=2000, null=True, blank=True)
    number=models.IntegerField(blank=True,null=True, default=0)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    video = models.FileField(null=True, blank=True)
    duration = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            import moviepy.editor as mp
            clip = mp.VideoFileClip(self.video.path)
            self.duration = int(clip.duration)
            clip.close()
        except Exception as e:
            print(f"Error getting video duration: {e}")

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=RichTextField(null=True, blank=True)
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if self.video and self.course:
            raise ValueError("Comment can only be linked to a video or a Course, not both.")
        super().save(*args, **kwargs)
    


class SubComment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    comment=models.ForeignKey(Comment, on_delete=models.CASCADE,null=True,blank=True)
    description=RichTextField(null=True, blank=True)

class Notes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=RichTextField(null=True, blank=True) 
    number=models.IntegerField(blank=True,null=True, default=0) 
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        foreign_key_count = sum([bool(getattr(self, f)) for f in ['video', 'module', 'course']])
        if foreign_key_count > 1:
            raise ValueError("Comment can only be linked to one of video, module, or Course.")
        super().save(*args, **kwargs) 

class UserProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    number_of_videos_watched = models.IntegerField(default=0)
    total_number_of_videos = models.IntegerField(default=0)
    last_video_watched = models.ForeignKey(
        Video,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="last video watched",
    )
    progress_percent = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        if self.total_number_of_videos == 0:
            self.progress_percent = 0
        else:
            self.progress_percent = (
                self.number_of_videos_watched / self.total_number_of_videos
            ) * 100
        super().save(*args, **kwargs)   


class CourseProgress(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    total_number_of_videos = models.IntegerField(default=0)
    number_of_videos_watched = models.IntegerField(default=0)
    total_number_of_users = models.IntegerField(default=0)
    total_progress_percent = models.FloatField(default=0)

    def calculate_progress_percent(self):
        if self.total_number_of_users == 0:
            self.total_progress_percent = 0
        else:
            self.total_progress_percent = (self.number_of_videos_watched / (self.total_number_of_videos * self.total_number_of_users)) * 100

    def save(self, *args, **kwargs):
        self.total_number_of_users = self.course.enroller_user.count()
        self.total_number_of_videos = self.course.video_set.count()
        self.number_of_videos_watched = sum([userprogress.number_of_videos_watched for userprogress in UserProgress.objects.filter(course=self.course)])
        self.calculate_progress_percent()
        super().save(*args, **kwargs)




class Quiz(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    start_time = models.DurationField(default=timedelta(seconds=0))
    pass_mark = models.FloatField(default=0)

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)

class Monitor(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    ip=models.CharField(max_length=2000,blank=True,null=True)
    country=models.CharField(max_length=2000,blank=True,null=True)
    city=models.CharField(max_length=2000,blank=True,null=True)
    region=models.CharField(max_length=2000,blank=True,null=True)
    timeZone=models.CharField(max_length=2000,blank=True,null=True)
    browser=models.CharField(max_length=2000,blank=True,null=True)
    browser_version=models.CharField(max_length=2000,blank=True,null=True)
    operating_system=models.CharField(max_length=2000,blank=True,null=True)
    device=models.CharField(max_length=2000,blank=True,null=True)
    language=models.CharField(max_length=2000,blank=True,null=True)
    screen_resolution=models.CharField(max_length=2000,blank=True,null=True)
    referrer=models.CharField(max_length=2000,blank=True,null=True)
    landing_page=models.CharField(max_length=2000,blank=True,null=True)
    timestamp=models.DateTimeField(default=timezone.now)