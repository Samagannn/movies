import django_filters
from django import forms

from django.contrib.auth.models import User

from movies.models import Product, Tag, Category


class MovieFilter(django_filters.FilterSet):
    date_range = django_filters.DateRangeFilter(field_name='data', empty_label='Please select a date',
                                                widget=forms.Select(attrs={'class': 'form-select'}))
    tags = django_filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(),
                                                widget=forms.Select(attrs={'class': 'form-select'}))
    author = django_filters.ModelChoiceFilter(queryset=User.objects.all(),
                                              widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Product
        fields = ('tags', 'category', 'author')
