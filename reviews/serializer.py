from rest_framework import serializers
from .models import ReviewModel
from django.contrib.auth.models import User
from authoruser.serializer import MoreInfoSerializer, UserSerializer  # Import serializers

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Include full user info
    userinfo = MoreInfoSerializer(source="user.moreinfo", read_only=True)  # Include MoreInfo

    class Meta:
        model = ReviewModel
        fields = ['id', 'text', 'created_at', 'updated_at', 'user', 'userinfo'] 