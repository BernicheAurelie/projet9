from django.urls import path
from . import views

urlpatterns = [
    path('', views.followers_list, name='followers')
]