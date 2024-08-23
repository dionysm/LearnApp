from django.urls import path
from . import views as views
from courses import views as course_views  # Import views from courses app
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from .views import register
urlpatterns = [
    # other paths
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Fügt die Login/Logout-URLs von Django hinzu
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', course_views.dashboard, name='dashboard'),
    path('courses/', course_views.courses, name='courses'),  # Correctly reference the courses app view
    path('learning-mode/', views.lernmodus_auswahl, name='learning_mode'),  # Use the LernApp view for this route
    path('learning-mode/start/', course_views.learning_mode, name='learning_mode_start'),  # Reference the correct view
    path('tests/', course_views.tests, name='tests'),
    path('profile/', course_views.profile, name='profile'),
    path('settings/', course_views.settings, name='settings'),
    path('<int:id>/', course_views.kurs_detail, name='kurs_detail'),  # Reference the correct view
]
