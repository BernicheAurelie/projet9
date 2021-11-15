from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from ticket.forms import CreateTicket
from ticket.models import Ticket
from review.forms import CreateReview
from review.models import Review


@login_required(login_url='connexion')
def createReview(request, ticket_id=None):
    if request.method == 'POST' and ticket_id is not None:
        ticket = Ticket.objects.get(id__exact=ticket_id)
        form = CreateReview(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            ticket.reviewed = True
            ticket.save()
            review_headline = form.cleaned_data.get('headline')
            messages.success(request, 'Votre critique: ' + review_headline)
            return redirect('flux')
    else:
        form = CreateReview()
    return render(request, 'review/review.html', {'form': form})

@login_required(login_url='connexion')
def createReviewAndTicket(request):
    if request.method == 'POST':
        ticket_form = CreateTicket(request.POST, request.FILES)
        review_form = CreateReview(request.POST)
        if ticket_form.is_valid() and review_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            ticket.reviewed = True
            ticket.save()
            messages.success(request, 'Votre ticket et votre critique sont postés ')
            return redirect('flux')
    else:
        ticket_form = CreateTicket(request.POST)
        review_form = CreateReview(request.POST)
    context = {'ticket_form': ticket_form, 'review_form': review_form}
    return render(request, 'review/ticket_and_review.html', context)

@login_required(login_url='connexion')
def delete_review(request, review_id: int):
    if request.method == 'GET':
        review = Review.objects.get(id__exact=review_id)
        review.delete()
        return redirect('flux')
    return render(request, 'posts/post_review_view.html')

@login_required(login_url='connexion')
def modifyreview(request, review_id: int):
    context={}
    review = Review.objects.get(id__exact=review_id)
    ticket = Ticket.objects.get(id__exact=review.ticket.id)
    if request.method == 'GET':
        form = CreateReview(instance=review)
        context = {'form': form}
    if request.method == 'POST':
        form = CreateReview(request.POST)
        if form.is_valid():
            review.ticket = ticket
            review.rating = form.cleaned_data['rating']
            review.headline = form.cleaned_data['headline']
            if form.cleaned_data['body'] is False:
                review.body = None
            elif form.cleaned_data['body'] is not None:
                review.body = form.cleaned_data['body']
            review.save()
            review_headline = form.cleaned_data.get('headline')
            messages.success(request, 'Votre ticket: ' + review_headline)
            return redirect('flux')     
    return render(request, 'review/review.html', context)