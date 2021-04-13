import django_filters
from django_filters import CharFilter, DateFilter
from .models import NpaDoc
from django import forms

class NpaFilter(django_filters.FilterSet):

    name = CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control first_input_text'
            }
        )
    )
    number = CharFilter(
        field_name='number',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control second_input_text'
            }
        )
    )
    date = DateFilter(
        field_name = 'date',
        widget=forms.DateInput(
            attrs = {
                'type': 'date',
                'class': 'form-control'
            }
        )
    )
    class Meta:
        model = NpaDoc
        fields = ()
