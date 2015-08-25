from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    
    user = models.OneToOneField(User)
    tutorial_grp = models.CharField(max_length=8)
    picture = models.ImageField(upload_to="userimg/", blank=True)
    
    def __unicode__(self):
        return self.user.username
        

