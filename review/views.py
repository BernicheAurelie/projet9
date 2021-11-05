from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from ticket.models import Ticket
from review.forms import CreateReview


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
