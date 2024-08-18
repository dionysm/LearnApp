from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Kurs, KursEinschreibung
from .utils import get_kurse_data

@login_required
def dashboard(request):
    kurse_data = get_kurse_data(request.user)
    return render(request, 'dashboard.html', kurse_data)


def courses(request):
    kurse_data = get_kurse_data(request.user)
    return render(request, 'courses.html', kurse_data)

def learning_mode(request):
    return render(request, 'learning_mode.html')

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
