from django.shortcuts import render
from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from ..models import User
# from ..serializer import UserSerializer


# To be completed

@api_view(["GET"])
def get_posts(request):
    pass

@api_view(["POST"])
def create_post(request):
    pass

@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
    pass
