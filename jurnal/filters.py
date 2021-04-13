import django_filters
from django_filters import CharFilter, DateFilter, ChoiceFilter, ModelChoiceFilter
from .models import Jurnal
from main.models import Name_job
from django import forms

class JurnalFilter(django_filters.FilterSet):
    name = CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    start_date = DateFilter(
        field_name = 'date',
        lookup_expr = 'gte',
        widget=forms.DateInput(
            attrs = {
                'type': 'date',
                'class': 'form-control jurnal_form_margin_right'
            }
        )
    )
    end_date = DateFilter(
        field_name = 'date',
        lookup_expr = 'lte',
        widget=forms.DateInput(
            attrs = {
                'type': 'date',
                'class': 'form-control jurnal_form_margin_right'
            }
        )
    )

    name_job = ModelChoiceFilter(
        queryset = Name_job.objects.all(),
        widget=forms.Select(
            attrs = {
                'class': 'form-control jurnal_form_margin_right'
            }
        )
    )
    class Meta:
        model = Jurnal
        fields = ()



    # def __init__(self, *args, **kwargs):
    #     super(JurnalFilter, self).__init__(*args, **kwargs)
    #     self.filters['name_job'].widgets=forms.Select(attrs={
    #         'class': 'form-control'
    #     })
