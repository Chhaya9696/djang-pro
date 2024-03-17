from django.db import models

# Create your models here.
class Stock(models.Model):
    proc_name=models.CharField(max_length=30)
    proc_price=models.FloatField()
    qty=models.IntegerField()

# Create your models here.
class student(models.Model):
     roll_no = models.IntegerField()
     name=models.CharField(max_length=30)
     email=models.EmailField()

def __str__(self):
    return self.name