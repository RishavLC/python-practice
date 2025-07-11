from django.urls import path
# from .views import hello,hi,hi_name
from .views import *


urlpatterns = [
    path('register', user_register, name="register"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),
    path('friend_delete/<int:pk>', friend_delete, name="friend_delete"),
    path('edit_friend/<int:pk>', update_friend, name="edit_friend"),
    path('add_friend', add_friend, name="add_friend"),
    path('hi', hi, name="hii"),
    path('hi/<str:name>/', hi_name, name="hi_name"),
    path('', home, name="home"),
]