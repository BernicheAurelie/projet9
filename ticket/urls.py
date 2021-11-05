from django.urls import path
from . import views

urlpatterns = [
    # path('tickets', views.list_tickets, name= 'list_tickets'),
    path('', views.createTicket, name= 'create_ticket')
]