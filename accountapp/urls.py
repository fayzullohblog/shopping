from django.urls import path
from .views import loginview,registerview,logoutview

urlpatterns = [
    path('login/',loginview,name='loginview'),
    path('register/',registerview,name='registerview'),
    path('logout/',logoutview,name='logoutview'),
]