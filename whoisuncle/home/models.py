from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    details = models.TextField(blank=True,null=True)
    reply = models.BooleanField(default=False)
    
def __str__(self):
    return self.title