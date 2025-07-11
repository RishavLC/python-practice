from django.urls import path
from .views import *

urlspatterns = [
    path('hello',hello, name = 'hello')
]