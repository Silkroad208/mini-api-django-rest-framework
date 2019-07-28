from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class FilterTokenMiddleware(MiddlewareMixin):
    allowed_tokens = ["123", ]

    def __call__(self, request):
        token = request.GET.get('token', None)

        if not token or token not in FilterTokenMiddleware.allowed_tokens:
            return HttpResponse('Unauthorized', status=401)

        return self.get_response(request)
