# Create your views here.
from rest_framework import parsers, renderers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class RemoveAuthToken(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def delete(self, request):
        if request.auth is not None:
            request.auth.delete()
            return Response(data={'description': 'Your session have finished'}, status=204, )


remove_auth_token = RemoveAuthToken.as_view()
