from django.db import models
from users.models import User  # Importiere das benutzerdefinierte User-Modell

class Kurs(models.Model):
    name = models.CharField(max_length=255)
    beschreibung = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kurse"


class Themenbereich(models.Model):
    name = models.CharField(max_length=255)
    beschreibung = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Themenbereich"
        verbose_name_plural = "Themenbereiche"


class Lernfeld(models.Model):
    kurse = models.ManyToManyField(Kurs, related_name='lernfelder')  # Ändere ForeignKey zu ManyToManyField
    themenbereiche = models.ManyToManyField(Themenbereich, related_name='lernfelder', blank=True)
    name = models.CharField(max_length=255)
    beschreibung = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subfields')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Lernfeld"
        verbose_name_plural = "Lernfelder"


class Frage(models.Model):
    lernfelder = models.ManyToManyField(Lernfeld, related_name='fragen')  # Fragen können auch mehreren Lernfeldern zugeordnet sein
    themenbereiche = models.ManyToManyField(Themenbereich, related_name='fragen')
    fragen_text = models.TextField()
    antwort_text = models.TextField()
    bild_datei = models.ImageField(upload_to='fragen_bilder/', blank=True, null=True)
    erklaerung = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='erstellte_fragen')
    erstellt_am = models.DateTimeField(auto_now_add=True)
    zuletzt_bearbeitet = models.DateTimeField(auto_now=True)
    freigegeben = models.BooleanField(default=False)

    def __str__(self):
        return self.fragen_text

    class Meta:
        verbose_name = "Frage"
        verbose_name_plural = "Fragen"


class AntwortOption(models.Model):
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE, related_name='antworten')
    antwort_text = models.TextField()
    ist_korrekt = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.frage.fragen_text} - {self.antwort_text}"

    class Meta:
        verbose_name = "Antwort"
        verbose_name_plural = "Antworten"


class Lernkarte(models.Model):
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE, related_name='lernkarten')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lernkarten')
    themenbereiche = models.ManyToManyField(Themenbereich, related_name='lernkarten')  # Lernkarten basieren auf spezifischen Themenbereichen
    wiederholungsstufe = models.IntegerField(default=0)
    letzte_wiederholung = models.DateTimeField(auto_now=True)
    naechste_wiederholung = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.frage.fragen_text} - Stufe: {self.wiederholungsstufe}"
    class Meta:
        verbose_name = "Lernkarte"
        verbose_name_plural = "Lernkarten"


class Test(models.Model):
    name = models.CharField(max_length=255)
    lernfelder = models.ManyToManyField(Lernfeld, related_name='tests')
    themenbereiche = models.ManyToManyField(Themenbereich, related_name='tests')
    ersteller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Test"
        verbose_name_plural = "Tests"


class TestFrage(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='test_fragen')
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE)
    reihenfolge = models.IntegerField()

    def __str__(self):
        return f"{self.test.name} - {self.frage.fragen_text}"

    class Meta:
        verbose_name = "Test-Frage"
        verbose_name_plural = "Test-Fragen"


class TestErgebnis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    richtig_beantwortete_fragen = models.IntegerField()
    gesamt_fragen = models.IntegerField()
    abgeschlossen_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.name} - {self.richtig_beantwortete_fragen}/{self.gesamt_fragen}"
    class Meta:
        verbose_name = "Test-Ergebnis"
        verbose_name_plural = "Test-Ergebnisse"


class FrageProtokoll(models.Model):
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE, related_name='protokolle')
    alter_wert = models.JSONField()
    neuer_wert = models.JSONField()
    aenderung_von = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    geaendert_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Änderung an Frage {self.frage.id} von {self.aenderung_von.username}"

    class Meta:
        verbose_name = "Frage-Protokoll"
        verbose_name_plural = "Fragen-Protokolle"


class LernmodusAktivitaet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    frage = models.ForeignKey(Frage, on_delete=models.CASCADE)
    bewertung = models.CharField(max_length=20, choices=[('einfach', 'Einfach'), ('geht_so', 'Geht so'), ('schwierig', 'Schwierig')])
    anzeige_zeit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.frage.fragen_text} - {self.bewertung}"

    class Meta:
        verbose_name = "Lernmodus-Aktivität"
        verbose_name_plural = "Lernmodus-Aktivitäten"

class KursEinschreibung(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='einschreibungen')
    kurs = models.ForeignKey('courses.Kurs', on_delete=models.CASCADE, related_name='einschreibungen')
    eingeschrieben_am = models.DateTimeField(auto_now_add=True)
    aktiv = models.BooleanField(default=True)  # Um den Status der Einschreibung zu kontrollieren

    def __str__(self):
        return f"{self.user.username} in {self.kurs.name}"

    class Meta:
        verbose_name = "Kurs-Einschreibung"
        verbose_name_plural = "Kurs-Einschreibungen"

