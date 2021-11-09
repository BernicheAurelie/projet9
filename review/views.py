from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect

from ticket.forms import CreateTicket
from ticket.models import Ticket
from review.forms import CreateReview
from ticket.views import createTicket

#
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

    # elif request.method == 'POST' and ticket_id is None:
    #     form1 = CreateTicket(request.POST)
    #     form2 = CreateReview(request.POST)
    #     if form1.is_valid() and form2.is_valid():
    #         ticket = form1.save(commit=False)
    #         ticket.user = request.user
    #         ticket.save()
    #         review = form2.save(commit=False)
    #         review.user = request.user
    #         review.ticket = ticket
    #         review.save()
    #         ticket_title = form1.cleaned_data.get('title')
    #         messages.success(request, 'Votre ticket: ' + ticket_title)
    #         review_headline = form2.cleaned_data.get('headline')
    #         messages.success(request, 'Votre critique: ' + review_headline)
    #         return redirect('flux')

 # elif request.method == 'POST' and ticket_id is None:
 #        ticket = createTicket(request)
 #        form = CreateReview(request.POST)
 #        if form.is_valid():
 #            review = form.save(commit=False)
 #            review.user = request.user
 #            review.ticket = ticket
 #            review.save()
 #            ticket.reviewed = True
 #            ticket.save()
 #            review_headline = form.cleaned_data.get('headline')
 #            messages.success(request, 'Votre critique: ' + review_headline)
 #            return redirect('flux')

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