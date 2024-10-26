from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import User
from ..serializer import UserSerializer
from ..utils import encodeJWT, decodeJWT

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
        
        # Encoding userDetails using JWT -> https://pyjwt.readthedocs.io/en/stable/
        result = encodeJWT(userInfo)

        print("------",result)
        result2 = decodeJWT('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiZmlyc3RuYW1lIjoiVGVzdCIsImxhc3RuYW1lIjoiVXNlciIsInVzZXJuYW1lIjoidGVzdFVzciIsInBhc3N3b3JkIjoiTm90IEhhc2hlZCJ9.8TC9flhRDacUvRsYg3s-2KCjUM8xaxSwMJ5a7FctSgA')
        print("====", result2)


    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    return Response(status=status.HTTP_200_OK)

    