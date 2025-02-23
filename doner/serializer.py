# serializers.py
from rest_framework import serializers
from .models import DonerModel
from authoruser.serializer import UserSerializer
from resiver.serializer import ResiverSerializer

class DonerSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    resiver = UserSerializer(read_only=True)
    post = ResiverSerializer(read_only=True)

    class Meta:
        model = DonerModel
        fields = ['id', 'sender', 'resiver', 'post']
