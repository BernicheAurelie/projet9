from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from followers.forms import AddFollowers

from followers.models import UserFollows
from django.contrib.auth.models import User


"""
    get user from username given in request.post, 
    if this user exists: get or create an UserFollows object (request.user, username)
    return followed user and connected user in context with related_name of models.
    return followers.html where input for username is
"""
@login_required(login_url='connexion')
def add_followers(request):
    context={}
    if request.POST:
        username = request.POST['username']
        user = User.objects.filter(username__exact=username).first()
        if user is not None:
            UserFollows.objects.get_or_create(user=request.user, followed_user=user)
            messages.success(request, user.username + ' ajouté avec succès à vos abonnements.')
        else:
            messages.success(request, "L'utilisateur n'existe pas.")
        return redirect('add_followers')
    # related_name of models
    context['following'] = UserFollows.objects.filter(user__exact=request.user)
    context['followed_by'] = UserFollows.objects.filter(followed_user__exact=request.user)
    return render(request, 'followers/followers.html', context)

"""
    get dynamicaly user with his id and 
    get object UserFollows with this user and connected user
    delete this object and return to followers page
"""
@login_required(login_url='connexion')
def delete_followers(request, followed_user_id: int):
    if request.method == 'GET':
        user = User.objects.get(id__exact=followed_user_id)
        followed_user = UserFollows.objects.get(
            user__exact = request.user, 
            followed_user__exact = user)
        followed_user.delete()
        messages.success(request, f'Vous ne suivez plus "{user.username}"')
        return redirect('add_followers')
    return render(request, 'followers/followers.html')


