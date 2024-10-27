from django.urls import path
from .views import user_auth, user_mgt

urlpatterns=[
    path('users/', user_mgt.get_users, name="get_users"),
    path('users/register', user_mgt.register_user, name="register_user"),
    path('users/<int:pk>', user_mgt.user_detail, name="user_detail"),
    path('users/login/', user_auth.user_login, name="login")
]
