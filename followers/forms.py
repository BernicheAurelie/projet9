from django.forms import ModelForm
from followers.models import UserFollows


class AddFollowers(ModelForm):
    class Meta:
        model = UserFollows
        fields = ['followed_user']
