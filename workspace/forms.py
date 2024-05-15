from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from movies.models import Product, Category, Tag


class MovieForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select a category'

    class Meta:
        model = Product
        fields = ('title', 'price', 'content', 'image', 'category', 'tags')

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'image': forms.FileInput(attrs={'accept': 'image/*', 'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))


class RegisterForm(BaseUserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Come up with a password'})
        self.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm the password'})

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Come up with a username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
        }


class ChangeProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email'
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 mt-1 mb-2 focus:outline-none focus:border-indigo-500 rounded-md py-2 px-4 block w-full placeholder-gray-500',
                'placeholder': 'Enter name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 mt-1 mb-2 focus:outline-none focus:border-indigo-500 rounded-md py-2 px-4 block w-full placeholder-gray-500',
                'placeholder': 'Enter last name'}),
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 mt-1 mb-5 focus:outline-none focus:border-indigo-500 rounded-md py-2 px-4 block w-full placeholder-gray-500',
                'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 mt-5 mb-5 focus:outline-none focus:border-indigo-500 rounded-md py-2 px-4 block w-full placeholder-gray-500',
                'placeholder': 'Enter email'}),
        }


class ChangePasswordForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user: User = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    password = forms.CharField(label='Current password', widget=forms.PasswordInput(attrs={
        'class': 'max-w-md mx-auto mt-1 mb-3 w-full border rounded-md p-2 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300',
    }))
    new_password = forms.CharField(label='New password', widget=forms.PasswordInput(attrs={
        'class': 'max-w-md mx-auto mt-1 mb-3 w-full border rounded-md p-2 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300',
    }), validators=[validate_password])
    confirm_password = forms.CharField(label='Confirm the password', widget=forms.PasswordInput(attrs={
        'class': 'max-w-md mx-auto mt-1 w-full border rounded-md p-2 text-gray-700 placeholder-gray-400 focus:outline-none focus:ring focus:border-blue-300',
    }))


def clean(self):
    data = self.cleaned_data

    password = data.get('password')
    new_password = data.get('new_password')
    confirm_password = data.get('confirm_password')

    errors = {}

    if not self.user.check_password(password):
        errors['password'] = ['The password is incorrect.']

    if new_password != confirm_password:
        errors['confirm_password'] = ['The passwords do not match.']

    if len(errors) > 0:
        raise forms.ValidationError(errors)

    return data
