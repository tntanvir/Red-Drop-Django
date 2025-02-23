from django.db import models
from django.contrib.auth.models import User
from resiver.models import ResiverModel

class DonerModel(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_donations')
    resiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_donations')
    post = models.ForeignKey(ResiverModel, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"Sender: {self.sender.username}, Resiver: {self.resiver.username}, Post ID: {self.post.id}"
 