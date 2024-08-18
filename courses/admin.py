from django.contrib import admin
from .models import (
    Kurs, Themenbereich, Lernfeld, Frage, AntwortOption, Lernkarte, Test, TestFrage,
    TestErgebnis, FrageProtokoll, LernmodusAktivitaet, KursEinschreibung
)

admin.site.register(Kurs)
admin.site.register(Themenbereich)
admin.site.register(Lernfeld)
admin.site.register(Frage)
admin.site.register(AntwortOption)
admin.site.register(Lernkarte)
admin.site.register(Test)
admin.site.register(TestFrage)
admin.site.register(TestErgebnis)
admin.site.register(FrageProtokoll)
admin.site.register(LernmodusAktivitaet)
admin.site.register(KursEinschreibung)