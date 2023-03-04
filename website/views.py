from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from user_agents import parse
# from geoip import geolite2
from .models import Course, Module, Video, Comment, SubComment, Notes,Monitor

# Create your views here.

def index(request):
    return render(request, 'main/base.html')


# def monitor(request):
#     if request.method == 'POST':
#         user_agent = request.META.get('HTTP_USER_AGENT', '')
#         parsed_user_agent = parse(user_agent)
#         monitor_data = {
#             'user': request.user,
#             'ip': request.META.get('REMOTE_ADDR', ''),
#             'country': '',
#             'city': '',
#             'region': '',
#             'timeZone': '',
#             'browser': parsed_user_agent.browser.family,
#             'browser_version': parsed_user_agent.browser.version_string,
#             'operating_system': parsed_user_agent.os.family,
#             'device': parsed_user_agent.device.family,
#             'language': request.META.get('HTTP_ACCEPT_LANGUAGE', ''),
#             'screen_resolution': '',
#             'referrer': request.META.get('HTTP_REFERER', ''),
#             'landing_page': request.build_absolute_uri(),
#             'timestamp': timezone.now(),
#         }
#         match = geolite2.lookup(monitor_data['ip'])
#         if match is not None:
#             monitor_data['country'] = match.country
#             monitor_data['city'] = match.city
#             monitor_data['region'] = match.subdivisions[0] if len(match.subdivisions) > 0 else ''
#             monitor_data['timeZone'] = match.timezone


#         if 'screen' in parsed_user_agent:
#             monitor_data['screen_resolution'] = f"{parsed_user_agent.screen.resolution_width}x{parsed_user_agent.screen.resolution_height}"


#         Monitor.objects.create(**monitor_data)

#     return render(request, 'monitor.html')