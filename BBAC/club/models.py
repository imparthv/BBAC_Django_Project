from django.db import models

# Create your models here.

# Represents members of club
class Member(models.Model):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('volunteer', 'Volunteer'),
        ('educator', 'Educator'),
        ('admin', 'Admin')

    ]
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    joined_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.name}({self.role})"
    
