from django.db import models

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
    
    def __str__(self):
        return self.name
