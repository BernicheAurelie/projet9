from django.forms import ModelForm
from review.models import Review
from django import forms


class CreateReview(ModelForm):
    class Meta:
        CHOICES = [
            (0, "- 0"),
            (1, "- 1"),
            (2, "- 2"),
            (3, "- 3"),
            (4, "- 4"),
            (5, "- 5"),
        ]
        model = Review
        fields = ["rating", "headline", "body"]
        widgets = {"rating": forms.RadioSelect(choices=CHOICES)}
