from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    Name = models.CharField(max_length=20)
    About = models.CharField(max_length= 50)
    Website = models.URLField(max_length=50)   
    
    def __str__(self):
        return self.Name                                                                              
    
class WatchList(models.Model):
    title = models.CharField(max_length=20)
    StoryLine = models.CharField(max_length=300)
    Platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE,related_name="WatchList")
    active = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

