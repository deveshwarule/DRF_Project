from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
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
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description = models.CharField(max_length=200,null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="Reviews")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.rating)+" | "+self.watchlist.title
                                            
                                            