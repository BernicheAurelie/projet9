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
    if request.method == 'GET':
        ticket = Ticket.objects.get(id__exact=ticket_id)
        print('--------> ticket: ', ticket)
        form = CreateTicket(instance=ticket)
        context = {'form': form}
        if request.method == 'POST':
            print('-------- on est dans la requete post ----------')
            form = CreateTicket(request.POST, request.FILES, instance=ticket)
            if form.is_valid():
                ticket = form.save()
                ticket_title = form.cleaned_data.get('title')
                messages.success(request, 'Votre ticket: ' + ticket_title)
                return redirect('flux')
            else:
                print('-------- form non valide ----------')
        print('-------- on est avant le return ----------')
        return render(request, 'ticket/ticket.html', context)
    return render(request, 'ticket/ticket.html', context)

    


