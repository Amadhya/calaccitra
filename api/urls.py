from django.urls import path

from api.views import *

urlpatterns = [
    path('check', Check, name='check'),
]