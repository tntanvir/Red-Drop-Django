from rest_framework import serializers
from .models import ResiverModel
from django.contrib.auth.models import User
from authoruser.serializer import UserSerializer


    

# class ResiverSerializer(serializers.ModelSerializer):
    
#     # user = UserMoreInfoSerializer(read_only=True)
#     class Meta:
#         model = ResiverModel
#         fields = ['id', 'number', 'location', 'blood_gp', 'date_from', 'date_to', 'more', 'resivedBool', 'user']

class ResiverSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = ResiverModel
        fields =  ['id', 'user','username','number', 'location', 'blood_gp', 'date_from', 'date_to', 'more', 'resivedBool']

   