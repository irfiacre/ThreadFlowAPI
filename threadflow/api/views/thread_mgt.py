from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Thread
from ..serializer import ThreadSerializer
from ..utils import CustomTokenAuthentication
from rest_framework.permissions import AllowAny

#{"title": "Test Thread", "description":"To test"}

@api_view(["GET", "POST"])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([AllowAny])
def manage_thread(request):
    threads = Thread.objects.all()
    serializer = ThreadSerializer(threads, many=True)
    if request.method == 'GET':
        return Response(serializer.data)
    if request.method == 'POST':
        request.data["user"] = request.user["user_id"]
        serializer = ThreadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "DELETE"])
@authentication_classes([CustomTokenAuthentication])
@permission_classes([AllowAny])
def thread_detail(request, pk):
    try:
        thread = Thread.objects.get(pk=pk)
        thread_information = ThreadSerializer(thread)
    except Thread.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        return Response(thread_information.data)
    
    if request.method == 'PUT':
        serializer = ThreadSerializer(thread, data=thread_information.data|request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        thread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
