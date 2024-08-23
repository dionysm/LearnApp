from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import CustomUserCreationForm
from users.forms import CustomUserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from courses.models import Lernfeld, Themenbereich, KursEinschreibung

def startseite(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Weiterleitung zum Dashboard, wenn der Benutzer eingeloggt ist
    return render(request, 'landing_page.html')  # Zeige die Landing Page für nicht eingeloggte Benutzer

#@login_required
#def dashboard(request):
#    kurse_data = get_kurse_data(request.user)
#    return render(request, 'dashboard.html', kurse_data)


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')  # Weiterleitung zum Dashboard nach der Registrierung
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def lernmodus_auswahl(request):
    # Kurse, in die der Benutzer eingeschrieben ist
    eingeschriebene_kurse = KursEinschreibung.objects.filter(user=request.user).select_related('kurs')

    # Themenbereiche (optional, falls sie nicht kursabhängig sind)
    themenbereiche = Themenbereich.objects.all()

    return render(request, 'auswahl_leaning_mode.html', {
        'eingeschriebene_kurse': eingeschriebene_kurse,
        'themenbereiche': themenbereiche,
        #'lernfeldname-short': eingeschriebene_kurse.Lernfeld.name
    })