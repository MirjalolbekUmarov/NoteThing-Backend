from django.db import models

# Create your models here.

class Note(models.Model):
    
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 500)
    
    added = models.DateTimeField(auto_now_add = True)
    
    def __str__(self) -> str:
        return str(self.title)