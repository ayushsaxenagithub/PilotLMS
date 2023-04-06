from django.db.models.signals import user_logged_in
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Monitor
from django.core.signals import response
from django.dispatch import receiver

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    monitor = Monitor()
    monitor.user = user
    monitor.ip = request.META.get('REMOTE_ADDR')
    monitor.country = request.META.get('GEOIP_COUNTRY_NAME')
    monitor.city = request.META.get('GEOIP_CITY')
    monitor.region = request.META.get('GEOIP_REGION_NAME')
    monitor.timeZone = request.META.get('GEOIP_TIME_ZONE')
    monitor.browser = request.META.get('HTTP_USER_AGENT')
    monitor.timestamp = timezone.now()
    monitor.save()

@receiver(response)
def log_user_activity(sender, request, response, **kwargs):
    if request.user.is_authenticated:
        monitor = Monitor()
        monitor.user = request.user
        monitor.ip = request.META.get('REMOTE_ADDR')
        monitor.country = request.META.get('GEOIP_COUNTRY_NAME')
        monitor.city = request.META.get('GEOIP_CITY')
        monitor.region = request.META.get('GEOIP_REGION_NAME')
        monitor.timeZone = request.META.get('GEOIP_TIME_ZONE')
        monitor.browser = request.META.get('HTTP_USER_AGENT')
        monitor.screen_resolution = request.META.get('HTTP_RESOLUTION')
        monitor.timestamp = timezone.now()
        monitor.save()
