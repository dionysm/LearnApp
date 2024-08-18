from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'data-toggle': 'tooltip',
        'title': 'Enter a valid email address.'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'title': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
            }),
            'email': forms.EmailInput(attrs={  # Hier wird das Widget für das E-Mail-Feld definiert
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'title': 'Enter a valid email address.'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'title': (
                    'Your password can’t be too similar to your other personal information.\n'
                    'Your password must contain at least 8 characters.\n'
                    'Your password can’t be a commonly used password.\n'
                    'Your password can’t be entirely numeric.'
                )
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'form-control',
                'data-toggle': 'tooltip',
                'title': 'Enter the same password as before, for verification.'
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
