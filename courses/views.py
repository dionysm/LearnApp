from django.shortcuts import render

def dashboard(request):
    return render(request, 'dashboard.html')

def courses(request):
    return render(request, 'courses.html')

def learning_mode(request):
    return render(request, 'learning_mode.html')

def tests(request):
    return render(request, 'tests.html')

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')
