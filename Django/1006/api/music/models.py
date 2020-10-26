from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.TextField()
    
    def __str(self):
        return self.name
    

class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.TextField()
    
    def __str(self):
        return self.title