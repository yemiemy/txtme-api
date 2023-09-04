from rest_framework.response import Response
from rest_framework.views import APIView
from chat.service.pusher import pusher_client
from django.conf import settings

# Create your views here.

class MessageAPIView(APIView):
    permission_classes = ()

    def post(self, request, *args, **kwargs):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message'],
        })

        return Response({})