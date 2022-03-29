from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group



from .serializers import EmployeeSerializer, UserSerializer, GroupSerializer
from .models import Employee

class EmployeeView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, employer_id, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        try:
            employer = Employee.objects.get(id=employer_id)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialier = EmployeeSerializer(employer, context={'request': request})
        return Response(serialier.data)

class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, user_id, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serialier = UserSerializer(user, context={'request': request})
        return Response(serialier.data)
