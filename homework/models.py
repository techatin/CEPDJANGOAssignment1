from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Homework(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='A homework to be done')
    subject = models.ForeignKey(Subject)
    
    given_date = models.DateField()
    due_date = models.DateField()
    
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)

    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"id":self.pk})
