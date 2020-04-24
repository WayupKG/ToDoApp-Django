from django.forms import ModelForm, TextInput, DateInput

from .models import Message, User


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'end_date']
        widgets = {
            'end_date': DateInput(attrs={
                'type': 'date',
                'name': 'end_date'
            })
        }