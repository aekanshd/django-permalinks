from django.conf.urls import url, include
from permalinks import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^permalinks/get-random-string/$', csrf_exempt(views.get_random_string.as_view())),
]