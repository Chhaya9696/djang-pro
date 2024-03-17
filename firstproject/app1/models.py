from django.db import models

class batch(models.Model):
    batchno=models.CharField(max_length=30,unique=True)
    time=models.CharField(max_length=20)
    module=models.CharField(max_length=20)
    labno=models.IntegerField()

def __str__(self):
    return self.module_name

class student(models.Model):
    rollno=models.IntegerField(max_length=20,unique=True)
    name=models.CharField(max_length=30)
    email=models.EmailField()

# class Feedback(models.Model):
#     username=models.CharField(max_length=30)
#     created_date=models.DateTimeField(auto_now_add=True)
#     feedback=models.TextField()