from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.username