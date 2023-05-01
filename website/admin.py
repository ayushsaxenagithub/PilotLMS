from django.contrib import admin
from .models import Tags, Course, Module, Video, Comment, SubComment, Notes, Monitor, UserProgress, CourseProgress, Quiz, Question, Answer, Enrollment

# Register your models here.

admin.site.register(Tags)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Notes)
admin.site.register(Monitor)
admin.site.register(UserProgress)
admin.site.register(CourseProgress)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Enrollment)



