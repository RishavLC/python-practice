from django.urls import path
from . import views
from.views import *

urlpatterns = [
    path('hi/', hi, name='hi'),
    path('', home, name="home"),
    path('add_book/', add_book, name="add_book"),
    path('update_book/<int:pk>', update_book, name="update_book"),
    path('delete_book/<int:pk>', delete_book, name="delete_book"),
    path('register/', views.user_register, name="register"),
    path('login', user_login, name="login"),
    path('logout', user_logout, name="logout"),
    
]
