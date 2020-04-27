from django import forms

from cricket.models import Kheladi


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Kheladi
        fields = ['first_name', 'last_name', 'bio', 'dob', 'dp', 'country', 'height', 'role',
                  'batting_style', 'bowling_style', 'highest_score', 'highest_wicket',]