from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import uuid
from django.utils import timezone
from user.models import Profile,Organization,Teacher,Student

class Tags(models.Model):
    name=models.CharField(max_length=2000,blank=True, null=True)
    
class Course(models.Model):
    name = models.CharField(max_length=2000,blank=True,null=True)
    organisation = models.ForeignKey(Organization, on_delete=models.CASCADE, null = True, blank = True)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE, blank=True, null=True)
    enroller_user=models.ManyToManyField(User,blank=True, null=True, through="Enrollment")
    tags=models.ManyToManyField(Tags, blank=True, null=True)
    description=RichTextField(null=True, blank=True)
    image_course=models.ImageField(null=True, blank=True, default='blank.png',upload_to='course/')
    price = models.DecimalField(null=True, blank=True, default=0, max_digits=100, decimal_places=2)
    small_description = models.TextField(null=True, blank=True)
    description=RichTextField(null=True, blank=True)
    learned = RichTextField(null = True, blank = True)
    created_at=models.DateTimeField(null=True, blank = True)
    updated_at=models.DateTimeField(null=True, blank =True)
    modules=models.IntegerField(null=True, blank = True)


class Enrollment(models.Model):
    course = models.ForeignKey(Course, related_name="enrollments",on_delete=models.CASCADE)
    student = models.ForeignKey(User, related_name="user_courses", on_delete=models.CASCADE)
    class Meta:
        unique_together = ('course', 'student')


class Module(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    number=models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=2000,blank=True,null=True)
    description=RichTextField(null=True, blank=True)

class Video(models.Model):
    module=models.ForeignKey(Module, on_delete=models.CASCADE, blank=True, null=True)
    video=models.FileField(null=True, blank=True)
    name=models.CharField(max_length=2000,null=True, blank=True)

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
    video = models.ForeignKey(Video, null=True, blank=True, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=True, blank=True, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        foreign_key_count = sum([bool(getattr(self, f)) for f in ['video', 'module', 'course']])
        if foreign_key_count > 1:
            raise ValueError("Comment can only be linked to one of video, module, or Course.")
        super().save(*args, **kwargs)  

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