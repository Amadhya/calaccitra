from django.urls import path

from api.views import *

urlpatterns = [
    path('check', Check, name='check'),
    path('login', login, name='login'),
    path('signup', signup, name='sign up'),
    path('movie', movie, name='movie details'),
    path('review/create', create_review, name='create review')
]