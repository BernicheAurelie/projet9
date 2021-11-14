from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from followers.forms import AddFollowers

from followers.models import UserFollows
from django.contrib.auth.models import User


@login_required(login_url='connexion')
def add_followers(request):
    context={}
    if request.POST:
        username = request.POST['username']
        # print(User.objects.get(username__exact=username))
        user = User.objects.filter(username__exact=username).first()
        if user is not None:
            UserFollows.objects.get_or_create(user=request.user, followed_user=user)
            messages.success(request, 'Utilisateur ajouté avec succès.')
        else:
            messages.success(request, "L'utilisateur n'existe pas.")
        return redirect('add_followers')
    context['following'] = UserFollows.objects.filter(user__exact=request.user)
    context['followed_by'] = UserFollows.objects.filter(followed_user__exact=request.user)
    return render(request, 'followers/followers.html', context)

@login_required(login_url='connexion')
def delete_followers(request, followed_user_id: int):
    if request.method == 'GET':
        user = User.objects.get(id__exact=followed_user_id)
        followed_user = UserFollows.objects.get(
            user__exact = request.user, 
            followed_user__exact = user)
        followed_user.delete()
        # message_succes = messages.success(request, "Vous ne suivez plus cet utilisateur", followed_user)
        return redirect('add_followers')
    return render(request, 'followers/followers.html')


