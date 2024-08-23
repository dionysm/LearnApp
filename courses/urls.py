from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('courses/', views.courses, name='courses'),
    path('learning-mode/', views.lernmodus_auswahl, name='learning_mode'),
    path('tests/', views.tests, name='tests'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('<int:id>/', views.kurs_detail, name='kurs_detail'),  # Detailseite für Kurse

]


