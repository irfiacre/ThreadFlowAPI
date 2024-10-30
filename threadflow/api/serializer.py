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

class UserLoginSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['username', 'password']
    # firstname=serializers.CharField(max_length=100, read_only=True)
    # lastname = serializers.CharField(max_length=100, read_only=True)
    # username = serializers.CharField(max_length=50)
    # password = serializers.CharField(max_length=100,  style={'input_type_password'})
    # role = serializers.CharField(max_length=20, default="user", read_only=True)
    # photo_url=serializers.CharField(max_length=500, read_only=True)
    # biography= serializers.CharField(max_length=500, read_only=True)
