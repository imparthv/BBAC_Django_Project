from django.db import models

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    join_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
