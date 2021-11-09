from django.urls import path
from . import views

urlpatterns = [
    # path('', views.createReview, name='create_review'),
    path('create/', views.createReviewAndTicket, name='create_review_and_ticket'),
    path('create/<int:ticket_id>/', views.createReview, name='create_review')
]