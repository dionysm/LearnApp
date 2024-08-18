# Register your models here.
from django.contrib import admin
from .models import User, Abzeichen, UserAbzeichen, Logs

admin.site.register(User)
admin.site.register(Abzeichen)
admin.site.register(UserAbzeichen)
admin.site.register(Logs)
