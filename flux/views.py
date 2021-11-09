from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from review.models import Review
from ticket.models import Ticket
from django.db.models import CharField, Value
from itertools import chain

# @login_required(login_url='connexion')
# def list_tickets(request):
#     tickets = Ticket.objects.all()
#     context = {'tickets': tickets}
#     return render(request, 'flux/flux.html', context)

@login_required(login_url='connexion')
def list_tickets(request):
    tickets = Ticket.objects.all()
    reviews = Review.objects.all()
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    # context = {'tickets': tickets, 'reviews': reviews}
    posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
    context = {'posts': posts}
    return render(request, 'flux/flux.html', context)

# @login_required(login_url='connexion')
# def list_tickets(request):
#     tickets = Ticket.objects.all()
#     reviews = Review.objects.all()
#     tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
#     reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
#     posts = sorted(
#         chain(reviews, tickets),
#         key=lambda post: post.time_created,
#         reverse=True
#     )
#     context = {'posts': posts}
#     return render(request, 'flux/flux.html', context)