from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Thread
from ..serializer import ThreadSerializer
from ..utils import CustomTokenAuthentication, decodeJWT
from rest_framework.permissions import AllowAny

#{"title": "Test Thread", "description":"To test"}

@api_view(["GET"])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([AllowAny])
def get_threads(request):
    threads = Thread.objects.all()
    serializer = ThreadSerializer(threads, many=True)
    return Response(serializer.data)

@api_view(["POST"])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([AllowAny])
def create_thread(request):
    print("--->", type(request.data), request.data)
    request.data
    # serializer = ThreadSerializer(data=request.data)
    # if serializer.is_valid():
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    Response(status=status.HTTP_200_OK)

@api_view(["GET", "PUT", "DELETE"])
def thread_detail(request, pk):
    try:
        thread = Thread.objects.get(pk=pk)
    except Thread.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = ThreadSerializer(thread, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
