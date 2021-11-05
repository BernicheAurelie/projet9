from django.urls import path
from . import views

urlpatterns = [
    # path('', views.createReview, name='create_review'),
    path('create/', views.createReview, name='create_review'),
    path('create/<int:ticket_id>/', views.createReview, name='create_review')
]