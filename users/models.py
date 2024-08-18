from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model
class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    # Vermeidung von Konflikten durch Setzen von related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
    )

    def __str__(self):
        return self.username


class Abzeichen(models.Model):
    name = models.CharField(max_length=255)
    beschreibung = models.TextField()
    bedingung = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Abzeichen"
        verbose_name_plural = "Abzeichen"


class UserAbzeichen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abzeichen')
    abzeichen = models.ForeignKey(Abzeichen, on_delete=models.CASCADE)
    erhalten_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.abzeichen.name}"
    class Meta:
        verbose_name = "User-Abzeichen"
        verbose_name_plural = "User-Abzeichen"


class Logs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    log_action = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.log_action} - {self.date_time}"
    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
