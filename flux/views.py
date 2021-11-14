from itertools import chain

from django.contrib.auth.decorators import login_required
from django.db.models import CharField, Value, Q
from django.shortcuts import render
from review.models import Review
from ticket.models import Ticket
from followers.models import UserFollows


@login_required(login_url='connexion')
def flux(request):
    followed_users = UserFollows.objects.filter(user__exact=request.user)
    tickets = Ticket.objects.filter(
        Q(user__id__in=followed_users.values_list('followed_user')) 
        | Q(user__exact=request.user)
        )
    reviews = Review.objects.filter(
        Q(user__id__in=followed_users.values_list('followed_user')) 
        | Q(user__exact=request.user)
        )
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
    context = {'posts': posts}
    return render(request, 'flux/flux.html', context)

@login_required(login_url='connexion')
def posts(request):
    tickets = Ticket.objects.filter(
        Q(user__exact=request.user)
        )
    reviews = Review.objects.filter(
        Q(user__exact=request.user)
        )
    tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
    reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
    posts = sorted(
            chain(reviews, tickets),
            key=lambda post: post.time_created,
            reverse=True
        )
    context = {'posts': posts}
    return render(request, 'posts/post.html', context)

# @login_required(login_url='connexion')
# def list_tickets(request):
#     tickets = Ticket.objects.all()
#     reviews = Review.objects.all()
#     tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
#     reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
#     posts = sorted(
#             chain(reviews, tickets),
#             key=lambda post: post.time_created,
#             reverse=True
#         )
#     context = {'posts': posts}
#     return render(request, 'flux/flux.html', context)

# @login_required(login_url='connexion')
# def list_tickets(request):
#     user = request.user
#     tickets = Ticket.objects.get(user__exact=user)
#     reviews = Review.objects.get(user__exact=user)
#     tickets = tickets.annotate(content_type=Value('TICKET', CharField()))
#     reviews = reviews.annotate(content_type=Value('REVIEW', CharField()))
#     posts = sorted(
#         chain(reviews, tickets),
#         key=lambda post: post.time_created,
#         reverse=True
#     )
#     context = {'posts': posts}
#     return render(request, 'flux/flux.html', context)
