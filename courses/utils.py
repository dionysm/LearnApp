from .models import Kurs

def get_kurse_data(user):
    meine_kurse = Kurs.objects.filter(einschreibungen__user=user)
    alle_kurse = Kurs.objects.exclude(id__in=meine_kurse.values_list('id', flat=True))
    anzahl_meine_kurse = meine_kurse.count()

    return {
        'meine_kurse': meine_kurse,
        'alle_kurse': alle_kurse,
        'anzahl_meine_kurse': anzahl_meine_kurse
    }
