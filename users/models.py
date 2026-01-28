from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    adress = models.CharField(max_length=60)
    phone = models.CharField(max_length=13)

    def __str__(self):
        return self.username

class EmailCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='email_codes')
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    experies_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.experies_at = timezone.now() + timezone.timedelta(minutes=2)