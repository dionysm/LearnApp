from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def startseite(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Weiterleitung zum Dashboard, wenn der Benutzer eingeloggt ist
    return render(request, 'landing_page.html')  # Zeige die Landing Page für nicht eingeloggte Benutzer

@login_required
def dashboard(request):
    return render(request, 'courses/dashboard.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Weiterleitung zum Dashboard nach der Registrierung
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
