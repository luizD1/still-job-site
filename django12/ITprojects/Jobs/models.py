from django.db import models

# Create your models here.
class JobVacancy(models.Model):
    job_name = models.CharField(max_length=50,unique=True)
    job_descrition = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now=False)

    
    def __str__(self):
        return self.job_name
        

class Application(models.Model):
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    email_address = models.EmailField(max_length=100,unique=True)
    mobile_number = models.CharField(max_length=11)
    
    nationality = models.CharField(max_length=200)
    

     
    def __str__(self):
        return self.email_address


    
