from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=40)
    
class Students(models.Model):
    std_name=models.CharField(max_length=30)
    mark=models.IntegerField()
    department=models.ForeignKey(Department,on_delete=models.CASCADE)