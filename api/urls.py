from django.urls import path

from api.views import *

urlpatterns = [
    path('check', Check, name='check'),
    path('login', login, name='login'),
    path('signup', signup, name='sign up'),
    path('movie/<uuid:movie_id>', movie_details, name='movie details'),
    path('movie/create', create_movie, name='create movie'),
    path('movie/search/<str:title>', search_movie, name='search movie'),
    path('review/create', create_review, name='create review')
]