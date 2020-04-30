from cloudinary.forms import CloudinaryFileField
from django import forms

from cricket.models import Kheladi, Gang


class PlayerForm(forms.ModelForm):
    # dp = CloudinaryFileField(
    #     options={
    #         'crop': 'thumb',
    #         'width': 200,
    #         'height': 700,
    #         'folder': 'avatars'
    #     }
    # )

    class Meta:
        model = Kheladi
        fields = ['first_name', 'last_name', 'bio', 'dob', 'dp', 'favourite_cricketer', 'country', 'height', 'role',
                  'batting_style', 'bowling_style', 'highest_score', 'highest_wicket', ]


class GangForm(forms.ModelForm):
    class Meta:
        model = Gang
        fields = ['in_mind']