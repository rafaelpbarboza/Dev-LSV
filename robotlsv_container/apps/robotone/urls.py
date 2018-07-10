from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from .models import MonitorizatorRobot
from .views import RobotModelViewSet

router = SimpleRouter()

#router.register(r'viewset', RobotModelViewSet, base_name='robot')

router.register(r'model', RobotModelViewSet )
urls = router.urls

urlpatterns = [
    # url(r'^$', RobotModelViewSet, name='robots'),
    # url(r'^(?P<pk>\d+)/$', RobotModelViewSet, name='robots_name'),
    # url(r'^cbv/$', snippet_view),
    # url(r'^cbv/(?P<pk>\d+)/$', snippet_view),
] + urls




# urlpatterns = [
#     url(r'^$', get_snippets, name= 'snippets'),
#     url(r'^(?P<pk>\d+)/$', get_snippets, name='snippets_retrieve'),
# ]


# from django.conf.urls import url
# from rest_framework.routers import SimpleRouter
#
# from pastebin.views import snippet_view, SnippetView, detail_view, list_view, update_view, delete_view, \
#     SnippetViewSet, SnippetModelViewSet
# from .views import get_snippets, MoritorizatorRobotModelViewSet, RobotModelViewSet
