from .models import Upcoming_Dives
from django import forms


class UpcommingDivesForm(forms.ModelForm):
    class Meta:
        model = Upcoming_Dives
        fields = ['title', 'date', 'location', 'content', 'image']
