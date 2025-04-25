from django.contrib.auth.models import AbstractUser
from django.db import models

class UserType(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    EDITOR = 'EDITOR', 'Editor'
    STUDENT = 'STUDENT', 'Student'
    TEACHER = 'TEACHER', 'Teacher'

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=10, choices=UserType.choices)
    phone_number = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
    
    def save(self, *args, **kwargs):
        if not self.username:
            prefix_map = {
                'ADMIN': 'AD-',
                'EDITOR': 'ED-',
                'STUDENT': 'ST-',
                'TEACHER': 'T-'
            }
            prefix = prefix_map[self.user_type]
            last_user = CustomUser.objects.filter(user_type=self.user_type).order_by('-username').first()
            if last_user and last_user.username[3:].isdigit():
                number = int(last_user.username[3:]) + 1
            else:
                number = 1
            self.username = f"{prefix}{str(number).zfill(4)}"
        super().save(*args, **kwargs)