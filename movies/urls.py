from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('movies/<int:id>', movies, name='movies'),
    path('search/', search, name='search'),
]