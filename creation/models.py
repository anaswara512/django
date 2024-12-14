from django.db import models

class Person(models.Model):
    firstname = models.CharField(max_length=100,blank=True,null=True)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()

def __str__(self):
    return self.firstname
    
