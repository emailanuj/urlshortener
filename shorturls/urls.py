from django.urls import path
from .views import MakeURL,Home
urlpatterns=[
    path('',MakeURL,name='MakeURL'),
    path('<str:token>',Home,name='Home'),
]