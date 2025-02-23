from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ReviewModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    text = models.TextField(max_length=100000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        ordering  = ['-updated_at','-created_at']
    