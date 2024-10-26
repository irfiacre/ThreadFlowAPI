from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializer import UserSerializer
from dotenv import load_dotenv

# {"username":"testUsr", "password":"Not Hashed"}

@api_view(["POST"])
def user_login(request):
    try:
        username = request.data['username']
        password=request.data['password']
        user = User.objects.get(username=username)
        userInfo = UserSerializer(user).data
        
        if password != userInfo['password']:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        print("------",userInfo)


    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK)

    