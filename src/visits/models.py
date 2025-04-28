from django.db import models

# Create your models here.
class PageVisit(models.Model):
    #invisible col 'id' which is PK.
    path = models.TextField(null=True, blank=True)
    timestamp = models.DateField(auto_now_add=True)