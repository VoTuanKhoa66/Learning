from rest_framework.permissions import IsAuthenticated
from WEB_MOVIE.helpers import custom_response
from user.serializer import UserAcountSerializer, UserAcountUpdateSerializer
from rest_framework import views

# Create your views here.
class UserAcountView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserAcountSerializer(request.user)	
        return custom_response('Get user successfully!', 'Success', serializer.data, 200)

    def put(self, request, *args, **kwargs):
        serializer = UserAcountUpdateSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return custom_response('Update user successfully!', 'Success', serializer.data, 200)
        return custom_response('Update user failed!', 'Error', serializer.errors, 400)
