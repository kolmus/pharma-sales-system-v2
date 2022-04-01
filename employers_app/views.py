from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from datetime import datetime, timedelta
import jwt

from .models import User
from Pharma_sales_system_2.settings import SECRET_KEY


# Create your views here.
class LoginView(APIView):
    """This view let log in with API

    Args:
        email (str): email as login
        password (str): password
    Returns:
        jwt (str): token
    """

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed("User not found!")

        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")

        payload = {"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=60), "iat": datetime.utcnow()}

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}
        return response


class LogoutView(APIView):
    """
    This view lets to logout with API
    """

    def post(self, request):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "success"}
        return response
