from django.conf.urls import url
from rest_framework.authtoken.views import ObtainAuthToken

from .views import RemoveAuthToken

urlpatterns = [
    url(r'^login/$', ObtainAuthToken.as_view()),
    url(r'^logout/$', RemoveAuthToken.as_view()),
]