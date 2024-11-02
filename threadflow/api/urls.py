from django.urls import path

from .views import user_auth
from .views import user_mgt
from .views import thread_mgt
from .views import  posts

urlpatterns=[
    path('users/', user_mgt.get_users, name="get_users"),
    path('users/register/', user_mgt.register_user, name="register_user"),
    path('users/<int:pk>/', user_mgt.user_detail, name="user_detail"),
    path('users/login/', user_auth.user_login, name="login"),
    path('thread/', thread_mgt.manage_thread, name="manage_thread"),
    path('thread/<int:pk>/', thread_mgt.thread_detail, name="thread_detail"),
    path('thread/<int:fk>/post/', posts.manage_post, name="manage_post"),
    path('thread/<int:fk>/post/<int:pk>/', posts.post_detail, name="post_detail"),

]
