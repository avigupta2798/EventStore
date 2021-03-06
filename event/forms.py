from django import forms

from .models import *

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('author', 'picture', 'title', 'content_text', 'created_date')
