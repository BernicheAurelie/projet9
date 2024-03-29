from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreerUtilisateur(UserCreationForm):
    """Define fields for UserCreationForm to register user"""

    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
