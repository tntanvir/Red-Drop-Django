
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ResiverModel(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_moreinfo")
    number=models.CharField(max_length=13,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    blood_gp=models.CharField(max_length=10)
    date_from=models.DateField()
    date_to=models.DateField()
    more=models.TextField()
    resivedBool=models.BooleanField(default=False)

    def __str__(self) :
        return f'{self.user.first_name}----{self.location}--{self.blood_gp}'