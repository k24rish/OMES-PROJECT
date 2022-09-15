from logging.handlers import DEFAULT_SOAP_LOGGING_PORT
from django.db import models

# Create your models here.


class department(models.Model):
    name = models.CharField(max_length=100,null=False)
   
    def __str__(self):
        return self.name
    
class role(models.Model):
    name = models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name
    
class empolyee(models.Model):
    first_name = models.CharField(max_length=100,null=False)
    last_name = models.CharField(max_length=100)
    sallary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey (role,on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date= models.DateField()
    dept = models.ForeignKey('department', on_delete=models.CASCADE)


def __str__(self):
        return  "%s %s %s" %(self.first_name,self.last_name,self.phone)
        