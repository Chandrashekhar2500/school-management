from django.db import models

# Create your models here.
class teachers(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    emp_id = models.IntegerField()
    def __str__(self):
        return self.firstname

class students(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    standard = models.IntegerField()
    std_id = models.IntegerField()
    def __str__(self):
        return self.firstname