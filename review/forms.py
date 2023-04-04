from django.forms import ModelForm
from review.models import Review
from django import forms
from django.utils.safestring import mark_safe

# class HorizontalRadioRenderer(forms.RadioSelect):
#   def render(self):
#     return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))

  # widgets = {
  #     "rating": forms.RadioSelect(renderer=HorizontalRadioRenderer, choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
  # }

class CreateReview(ModelForm):
    class Meta:
        CHOICES = [(0, '- 0'), (1, '- 1'), (2, '- 2'), (3, '- 3'), (4, '- 4'), (5, '- 5')]
        model = Review
        fields = ['rating', 'headline', 'body']
        widgets = {
            "rating": forms.RadioSelect(choices=CHOICES)
        }
