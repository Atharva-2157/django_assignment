from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    addr1 = models.TextField()
    mobNo = models.CharField(max_length=10)
    mail = models.EmailField()
    
    def __str__ (self) -> str:
        return f"{self.name}"
