from django.contrib import admin
from .models import Tags, Course, Module, Video, Comment, SubComment, Notes, Monitor

# Register your models here.

admin.site.register(Tags)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(SubComment)
admin.site.register(Notes)
admin.site.register(Monitor)


