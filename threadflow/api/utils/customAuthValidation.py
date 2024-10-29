from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get("Authorization")
        if not token:
            return None  # No token, fallback to other authentication if any
        
        if token != "xxx":
            raise AuthenticationFailed("Invalid token")

        try:
            user = User.objects.get(username="jdoe")  # Adjust to match your logic
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found")

        return (user, None)