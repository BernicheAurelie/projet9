from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from ticket.forms import CreateTicket
from ticket.models import Ticket
#
#
# @login_required(login_url='connexion')
# def list_tickets(request):
#     tickets = Ticket.objects.all()
#     context = {'tickets': tickets}
#     return render(request, 'ticket/ticket_view.html', context)

@login_required(login_url='connexion')
def createTicket(request):
    if request.method == 'POST':
        form = CreateTicket(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            ticket_title = form.cleaned_data.get('title')
            messages.success(request, 'Votre ticket: ' + ticket_title)
            return redirect('flux')
    else:
        form = CreateTicket()
    context = {'form': form}
    return render(request, 'ticket/ticket.html', context)

@login_required(login_url='connexion')
def deleteTicket(request, ticket_id: int):
    if request.method == 'POST':
        ticket = Ticket.objects.get(id__exact=ticket_id)
        ticket.delete()
        return redirect('flux')
    return render(request, 'ticket/ticket_view.html')



