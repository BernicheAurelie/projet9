from django.urls import path
from . import views


urlpatterns = [
    path("", views.add_followers, name="add_followers"),
    path(
        "delete_followers/<int:followed_user_id>/",
        views.delete_followers,
        name="delete_followers",
    ),
]
