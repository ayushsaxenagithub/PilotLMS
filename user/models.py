from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.


# class Profile(models.Model):
#     user=models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
#     type=models.CharField(max_length=2000,blank=True,null=True, default="Student")
#     image_profile=models.ImageField(null=True, blank=True, default='blank.png',upload_to='user_profile/')
#     detail=models.TextField(blank=True,null=True)
#     id = models.UUIDField(default= uuid.uuid4, unique=True , primary_key=True, editable=False)

#     def __str__(self):
#         return str(self.name)



# Create your models here.
