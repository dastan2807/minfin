from django import forms
from .models import Jurnal
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from datetime import date
from django.contrib import messages

class JurnalForm(forms.ModelForm):
    class Meta:
        messages = date.today()
        model = Jurnal
        fields = "__all__"
        widgets = {
            'date': forms.DateInput(attrs={
                'type': "date",
                'value': messages,
                'min': messages,
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class AutoRegisterForm(AuthenticationForm ,forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
