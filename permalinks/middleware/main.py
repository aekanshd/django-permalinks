from permalinks.models import Permalinks
from django.http import HttpResponseRedirect

class PermalinksMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        try:
          old_url_object = Permalinks.objects.get(old_url=request.build_absolute_uri())
          return HttpResponseRedirect(old_url_object.new_url)
        except Exception as e:
          return response