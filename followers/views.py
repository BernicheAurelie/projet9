from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from followers.forms import AddFollowers

from followers.models import UserFollows
from users.models import User


@login_required(login_url='connexion')
def add_followers(request):
    context={}
    if request.POST:
        username = request.POST['username']
        user = User.objects.get(username__exact=username)
        if user is not None:
            UserFollows.objects.create(user=request.user, followed_user=user)
            messages.success(request, 'utilisateur ajouté')
        else:
            messages.success(request, "utilisateur n'existe pas")
        return redirect('add_followers')
    context['following'] = UserFollows.objects.filter(user__exact=request.user)
    context['followed_by'] = UserFollows.objects.filter(followed_user__exact=request.user)
    return render(request, 'followers/followers.html', context)

# @login_required(login_url='connexion')
# def delete_followers(request, followed_user_id: int):
#     if request.method == 'POST':
#         followed_user = UserFollows.objects.get(id__exact=followed_user_id)
#         followed_user.delete()
#         return redirect('add_followers')
#     return render(request, 'followers/followers.html')


