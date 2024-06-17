from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Person(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=20)
    age=models.IntegerField()
    dob=models.DateField()  
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    
    # foreign key relation
        
class Department(models.Model):
    name=models.CharField(max_length=40)
    
    def __str__(self):
        return self.name
    
class Employee(models.Model):
    name=models.CharField(max_length=45)
    age=models.IntegerField()
    salary=models.DecimalField(max_digits=12, decimal_places=2)
    department=models.ForeignKey(Department,on_delete=models.CASCADE, related_name='employees')
    
    def __str__(self):
        return f"{self.name}"
    
    #OneToOne relation
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.TextField()
    
    def __str__(self):
        return self.user.username
    
#ManyToMany Field

class Project(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Developers(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    project=models.ManyToManyField(Project,related_name='developers')
    
    def __str__(self):
        return f"{self.first_name}{self.last_name}"