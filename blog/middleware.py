import os

from django.http import HttpResponseForbidden


class AdminIPRestrictorMiddleware:
    """
    Middleware to restrict access to the Django admin interface based on client IP address.
    Only requests originating from IP addresses listed in `self.allowed_ips` are allowed to access any URL starting with '/admin/'.
    If a request to the admin interface comes from a disallowed IP, an HTTP 403 Forbidden response is returned.
    Attributes:
        get_response (callable): The next middleware or view in the Django request/response cycle.
        allowed_ips (list): List of IP addresses permitted to access the admin interface.
    Methods:
        __init__(get_response): Initializes the middleware with the next response handler.
        __call__(request): Processes each request, restricting admin access based on client IP.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_ips = os.getenv('ALLOWED_IPS', '').split(',')  # Define your allowed IPs here

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            client_ip = request.META.get('REMOTE_ADDR')
            if client_ip not in self.allowed_ips:
                return HttpResponseForbidden("Access denied from this IP address.")
        response = self.get_response(request)
        return response