from django.forms import ModelForm
from ticket.models import Ticket


class CreateTicket(ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
