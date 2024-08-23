from django.contrib import messages
from .utils import get_kurse_data
from django.shortcuts import render, get_object_or_404, redirect
from .models import Kurs, KursEinschreibung, Lernfeld, Themenbereich
from django.contrib.auth.decorators import login_required

# courses/views.py
from django.shortcuts import render

def courses(request):
    return render(request, 'courses/courses.html')

def learning_mode(request):
    return render(request, 'courses/learning_mode.html')

def tests(request):
    return render(request, 'courses/tests.html')

def profile(request):
    return render(request, 'courses/profile.html')

def settings(request):
    return render(request, 'courses/settings.html')

def kurs_detail(request, id):
    # Logic to fetch course details by id
    return render(request, 'courses/kurs_detail.html')


@login_required
def dashboard(request):
    kurse_data = get_kurse_data(request.user)
    return render(request, 'dashboard.html', kurse_data)



def courses(request):
    kurse_data = get_kurse_data(request.user)
    return render(request, 'courses.html', kurse_data)

@login_required
def lernmodus_auswahl(request):
    # Kurse, in die der Benutzer eingeschrieben ist
    eingeschriebene_kurse = KursEinschreibung.objects.filter(user=request.user).select_related('kurs')

    # Themenbereiche (optional, falls sie nicht kursabhängig sind)
    themenbereiche = Themenbereich.objects.all()

    return render(request, 'auswahl_learning_mode.html', {
        'eingeschriebene_kurse': eingeschriebene_kurse,
        'themenbereiche': themenbereiche
    })

@login_required
def learning_mode(request):
    # Verarbeite die Auswahl aus dem Auswahlbildschirm
    ausgewählte_lernfelder = request.GET.getlist('lernfelder')
    ausgewählte_themenbereiche = request.GET.getlist('themenbereiche')

    lernfelder = Lernfeld.objects.filter(id__in=ausgewählte_lernfelder)
    themenbereiche = Themenbereich.objects.filter(id__in=ausgewählte_themenbereiche)

    # Hier würdest du die Lernfragen für die gewählten Felder und Bereiche laden
    fragen = []  # Placeholder: Deine Logik für die Fragen

    return render(request, 'learning_mode.html', {
        'lernfelder': lernfelder,
        'themenbereiche': themenbereiche,
        'fragen': fragen,
    })

def tests(request):
    return render(request, 'tests.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')
@login_required
def kurs_detail(request, id):
    kurs = get_object_or_404(Kurs, id=id)

    # Überprüfen, ob der Benutzer bereits eingeschrieben ist
    eingeschrieben = KursEinschreibung.objects.filter(user=request.user, kurs=kurs).exists()

    if request.method == 'POST':
        if not eingeschrieben:
            # Benutzer in den Kurs einschreiben
            KursEinschreibung.objects.create(user=request.user, kurs=kurs)
            messages.success(request, f"Du hast dich erfolgreich in den Kurs '{kurs.name}' eingeschrieben!")
        else:
            messages.info(request, f"Du bist bereits in diesem Kurs eingeschrieben.")

        return redirect('kurs_detail', id=kurs.id)

    return render(request, 'courses/kurs_detail.html', {'kurs': kurs, 'eingeschrieben': eingeschrieben})
