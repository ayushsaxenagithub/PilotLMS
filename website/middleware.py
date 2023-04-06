from .signals import log_user_activity

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        log_user_activity(sender=None, request=request)
        return response
