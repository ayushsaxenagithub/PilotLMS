from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('logout/',views.logoutUser,name='logout'),
    path('register/', views.registerUser, name='register'),  
    path('update_profile/', views.update_profile, name='update_profile'),  
    path('profile/<uuid:profile_id>/',views.profile_detail, name='profile_detail'),
    path('coursebase/', views.coursebase, name='coursebase')
]

