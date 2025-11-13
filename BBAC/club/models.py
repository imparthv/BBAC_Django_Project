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
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    event_date = models.DateField()
    location = models.CharField(max_length=255)
    created_by = models.ForeignKey(Member, on_delete=models.CASCADE, related_name = 'events_crated')

    def __str__(self):
        return f'{self.title}({self.date.strftime('%d-%m-%Y')})'

class Participation(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('member', 'event') # prevents duplicate participation

    def __str__(self):
        status = "Attend" if self.attended else "Registered"
        return f"{self.member.name} - {self.event.title}({status})"



    
