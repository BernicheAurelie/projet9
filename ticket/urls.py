from django.urls import path
from . import views

urlpatterns = [
    # path('tickets', views.list_tickets, name= 'list_tickets'),
    path('delete_ticket/<int:ticket_id>/', views.deleteTicket, name='delete_ticket'),
    path('modify_ticket/<int:ticket_id>/', views.modifyTicket, name='modify_ticket'),

    path('', views.createTicket, name= 'create_ticket')
]
