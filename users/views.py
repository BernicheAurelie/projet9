from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreerUtilisateur


def inscriptionPage(request):
    """Use user form to register new user"""
    form = CreerUtilisateur()
    if request.method == "POST":
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Compte créé avec succès pour " + user)
            return redirect("connexion")
    context = {"form": form}
    return render(request, "users/inscription.html", context)


def accesPage(request):
    """Get informations from request to authenticate user"""
    context = {}
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("flux")
        else:
            messages.info(request, "Utilisateur ou mot de passe incorrect")
    return render(request, "users/acces.html", context)


def logoutUser(request):
    """Log out user and return to connexion page: users/acces.html"""
    logout(request)
    return redirect("connexion")
