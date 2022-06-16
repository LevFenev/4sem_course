from django.db import models
from simple_history.models import HistoricalRecords

class Post(models.Model):
    heading=models.CharField(max_length=100)
    description=models.TextField()
    type=models.ForeignKey('Type',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    history=HistoricalRecords()
    
    def __str__(self):
        return self.heading


class Type(models.Model):
    name=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    history=HistoricalRecords()
    
    def __str__(self):
        return self.name