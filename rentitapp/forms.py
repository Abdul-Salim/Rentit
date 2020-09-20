from django import forms
from .models import Profile,Vehicles
from django.contrib.auth.models import User
class VehiclesForm(forms.ModelForm):
    S_desc = forms.CharField(max_length=150,required=False)
    type = [('cars','Cars'),('bikes','Bikes'),('others','Others'),]
    tov = forms.CharField(max_length=150, widget=forms.Select(choices=type))
    class Meta:
        model = Vehicles
        labels = {
            'tov': 'type of vehicle'
        }

        fields = [
            'tov',
            'Adtitle',
            'brand',
            'cost',
            'DOM',
            'S_desc',
            'img1',
        ]
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']

