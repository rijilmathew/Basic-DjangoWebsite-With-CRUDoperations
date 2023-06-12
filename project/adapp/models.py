from django.db import models


# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=25,blank=False,null=False)
    email=models.EmailField()
    # age=models.IntegerField()
    age = models.IntegerField(blank=True, null=True)
    gender=models.CharField(max_length=25,blank=False,null=False)
    
    def __str__(self):
        return self.name
   
