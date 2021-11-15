from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from ticket.forms import CreateTicket
from ticket.models import Ticket


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
    if request.method == 'GET':
        ticket = Ticket.objects.get(id__exact=ticket_id)
        ticket.delete()
        return redirect('flux')
    return render(request, 'posts/post_ticket_view.html')

@login_required(login_url='connexion')
def modifyTicket(request, ticket_id: int):
    context={}
    ticket = Ticket.objects.get(id__exact=ticket_id)
    if request.method == 'GET':
        form = CreateTicket(instance=ticket)
        context = {'form': form}
    if request.method == 'POST':
        form = CreateTicket(request.POST, request.FILES)
        if form.is_valid():
            ticket.title = form.cleaned_data['title']
            ticket.description = form.cleaned_data['description']
            if form.cleaned_data['image'] is False:
                ticket.image = None
            elif form.cleaned_data['image'] is not None:
                ticket.image = form.cleaned_data['image']
            ticket.save()
            ticket_title = form.cleaned_data.get('title')
            messages.success(request, 'Votre ticket: ' + ticket_title)
            return redirect('flux')     
    return render(request, 'ticket/ticket.html', context)

    


