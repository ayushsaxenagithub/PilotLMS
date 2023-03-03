from django.contrib import admin
from .models import Profile, Organization, Teacher, Student

# Register your models here.

admin.site.register(Profile)
admin.site.register(Organization)
admin.site.register(Teacher)
admin.site.register(Student)