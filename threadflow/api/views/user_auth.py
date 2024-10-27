from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializer import UserSerializer
from ..utils import encodeJWT
from django.contrib.auth.hashers import check_password


# {"username":"jdoe", "password":"12345"}

@api_view(["POST"])
def user_login(request):
    try:
        username = request.data['username']
        password=request.data['password']
        user = User.objects.get(username=username)
        userInfo = UserSerializer(user).data
        if not check_password(password, userInfo['password']):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        result = {"Token":encodeJWT(userInfo)}
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK, data=result)
