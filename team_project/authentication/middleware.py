from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.request import Request


class AddTokenHeaderMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        token = AccessToken.for_user(request.user)
        request.headers['Authorization'] = f'Bearer {str(token)}'

        response = self.get_response(request)

        return response
