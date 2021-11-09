from django.urls import path
from . import views

urlpatterns = [
    # path('', views.followers_list, name='followers'),
    path('', views.add_followers, name='add_followers'),
    path('delete/<int:followed_user_id>/', views.delete_followers, name='delete_followers'),
    # path('delete/', views.delete_followers, name='delete_followers')
]