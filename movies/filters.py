import django_filters
from django import forms
from django.contrib.auth.models import User
from movies.models import Product, Tag, Category

class MovieFilter(django_filters.FilterSet):
    date_range = django_filters.DateRangeFilter(
        field_name='data',
        empty_label='Please select a date',
        widget=forms.Select(attrs={
            'class': 'w-full bg-white border rounded-md shadow-sm py-2 px-4 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300 mb-5'
        })
    )

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'flex flex-wrap space-x-2 mb-2'
        })
    )

    category = django_filters.ModelChoiceFilter(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full bg-white border rounded-md shadow-sm py-2 px-4 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300 mb-5'
        })
    )

    author = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={
            'class': 'w-full bg-white border rounded-md shadow-sm py-2 px-4 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300 mb-5'
        })
    )

    class Meta:
        model = Product
        fields = ('tags', 'category', 'author')
