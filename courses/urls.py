from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('courses/', views.courses, name='courses'),
    path('learning-mode/', views.learning_mode, name='learning_mode'),
    path('tests/', views.tests, name='tests'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
]