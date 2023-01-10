from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return f'{self.name}'
    
class Employers(models.Model):
    first_name = models.CharField(max_length=15,required=True)
    last_name = models.CharField(max_length=15,required=True)
    title = models.CharField(max_length=15,required=True)
    gender = models.CharField(max_length=15,required=True)
    is_staffed = models.BooleanField()
    start_date = models.DateField(auto_now=True)