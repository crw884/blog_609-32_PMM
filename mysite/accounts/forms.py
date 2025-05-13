from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth import password_validation

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={
        'placeholder': 'Логин',
        'autofocus': True,
        'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Пароль','autocomplete': 'current-password' , 'class': 'form-control'})
    )

class SignupForm(UserCreationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Логин',
            'autofocus': True,
            'class': 'form-control'
        })
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Пароль',
            'autocomplete': 'new-password',
            'class': 'form-control'}
        ),
        help_text=password_validation.password_validators_help_text_html()
    )
    password2 = forms.CharField(

        label='Password confirmation',
        required=True,
        strip=False,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Повторный пароль',
            'autocomplete': 'new-password',
            'class': 'form-control'}
        ),
        help_text='Введите пароль повторно.'
    )