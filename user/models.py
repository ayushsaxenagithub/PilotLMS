from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from ckeditor.fields import RichTextField
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    email = models.CharField(max_length=2000, blank=True, null=True)
    name = models.CharField(max_length=2000, blank=True, null=True)
    phone = models.CharField(max_length=2000, blank=True, null=True)
    status_choices = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
        ('Organization', 'Organization')
    )
    status = models.CharField(max_length=2000, choices=status_choices, blank=True, null=True, default='Student')
    image_profile = models.ImageField(null=True, blank=True, default='blank.png', upload_to='user_profile/')
    shortBio = models.CharField(max_length=2000, blank=True, null=True)
    detail = RichTextField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Organization(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    description = RichTextField(blank=True, null=True)
    location = models.CharField(max_length=2000, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    founded_year = models.IntegerField(blank=True, null=True)
    employees = models.IntegerField(blank=True, null=True)


class Teacher(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)
    department = models.CharField(max_length=2000, blank=True, null=True)
    qualification = models.CharField(max_length=2000, blank=True, null=True)
    bio = RichTextField(blank=True, null=True)    
    date_of_birth = models.DateField(blank=True, null=True)
    research_interests = RichTextField(blank=True, null=True)


class Student(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    department = models.CharField(max_length=2000, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
