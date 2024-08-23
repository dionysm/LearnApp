from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Richtiges Modell verwenden
User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'data-toggle': 'tooltip',
        'title': 'Enter a valid email address.'
    }))

    class Meta:
        model = User  # Hier das richtige Modell verwenden
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Explizite Zuweisung der Klasse für jedes Feld
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'data-toggle': 'tooltip',
            'title': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'data-toggle': 'tooltip',
            'title': 'Enter a valid email address.'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'data-toggle': 'tooltip',
            'title': (
                'Your password can’t be too similar to your other personal information.\n'
                'Your password must contain at least 8 characters.\n'
                'Your password can’t be a commonly used password.\n'
                'Your password can’t be entirely numeric.'
            )
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'data-toggle': 'tooltip',
            'title': 'Enter the same password as before, for verification.'
        })
