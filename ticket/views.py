from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from ticket.forms import CreateTicket
from ticket.models import Ticket


@login_required(login_url="connexion")
def createTicket(request):
    """Create ticket with associated form and save it."""
    title = "Créer un ticket"
    if request.method == "POST":
        form = CreateTicket(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            ticket_title = form.cleaned_data.get("title")
            messages.success(
                request, "Votre ticket: " + ticket_title + " a bien été créé"
            )
            return redirect("flux")
    else:
        form = CreateTicket()
    context = {"form": form, "title": title}
    return render(request, "ticket/ticket.html", context)


@login_required(login_url="connexion")
def deleteTicket(request, ticket_id: int):
    """Get ticket by id and delete it."""
    if request.method == "GET":
        ticket = Ticket.objects.get(id__exact=ticket_id)
        ticket.delete()
        messages.success(request, "Publication supprimée avec succès")
        return redirect("flux")
    return render(request, "posts/post_ticket_view.html")


@login_required(login_url="connexion")
def modifyTicket(request, ticket_id: int):
    """Get ticket by id, call form with it in instance and save new form"""
    title = "Modifier votre ticket"
    ticket = Ticket.objects.get(id__exact=ticket_id)
    context = {"title": title, "ticket": ticket}
    if request.method == "GET":
        form = CreateTicket(instance=ticket)
        context = {"form": form, "title": title, "ticket": ticket}
    if request.method == "POST":
        form = CreateTicket(request.POST, request.FILES)
        if form.is_valid():
            ticket.title = form.cleaned_data["title"]
            ticket.description = form.cleaned_data["description"]
            if form.cleaned_data["image"] is False:
                ticket.image = None
            elif form.cleaned_data["image"] is not None:
                ticket.image = form.cleaned_data["image"]
            ticket.save()
            messages.success(request, "Votre ticket a bien été modifié")
            return redirect("flux")
    return render(request, "ticket/ticket.html", context)
