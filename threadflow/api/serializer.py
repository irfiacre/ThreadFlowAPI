from rest_framework import serializers
from .models import User, Post, Thread

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Thread
        fields = '__all__'
