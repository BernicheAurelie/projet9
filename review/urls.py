from django.urls import path
from . import views

urlpatterns = [
    # path('', views.createReview, name='create_review'),
    path('create/', views.createReviewAndTicket, name='create_review_and_ticket'),
    path('create/<int:ticket_id>/', views.createReview, name='create_review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('modify_review/<int:review_id>/', views.modifyreview, name='modify_review'),
]
