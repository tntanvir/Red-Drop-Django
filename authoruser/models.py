from django.db import models
from django.contrib.auth.models import User



class MoreInfo(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name='moreinfos')
    image = models.URLField(max_length=200)
    name=models.CharField(max_length=30)
    phone=models.CharField(max_length=13)
    location=models.CharField(max_length=200)
    blood_group=models.CharField(max_length=10)

    def __str__(self):
        return self.name