
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import MoreInfo
from django.contrib.auth import get_user_model

User = get_user_model()



class Registerseializer(serializers.ModelSerializer):
    # password1 =serializers.CharField(max_length=100)
    password2 =serializers.CharField(max_length=100)
    image =serializers.CharField(max_length=200)
    name =serializers.CharField(max_length=30)
    phone =serializers.CharField(max_length=13)
    location =serializers.CharField(max_length=200)
    blood_group=serializers.CharField(max_length=10)
    class Meta:
        model = User
        fields = ['image', 'username', 'email','name','phone','location','blood_group', 'password','password2']

    def save(self):
        image = self.validated_data['image']
        username = self.validated_data['username']
        email = self.validated_data['email']
        name = self.validated_data['name']
        phone = self.validated_data['phone']
        location = self.validated_data['location']
        blood_group = self.validated_data['blood_group']
        password = self.validated_data['password']
        password2= self.validated_data['password2']
        if password2!=password:
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'username': 'Username already exists'})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})
        user = User(username=username, email=email)
        user.set_password(password)
        user.is_active=False
        user.save()
        moreinfo = MoreInfo(image=image, user=user, name=name,phone=phone,location=location,blood_group=blood_group)
        moreinfo.save()
        return user

class loginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)       




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class MoreInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = MoreInfo
        fields = ['id','user', 'image', 'name', 'phone', 'location', 'blood_group']


class MoreInfoSerializers(serializers.ModelSerializer):
   

    class Meta:
        model = MoreInfo
        fields = ['image', 'name', 'phone', 'location', 'blood_group']



class UserSerializer(serializers.ModelSerializer):
    moreinfo = MoreInfoSerializers(source='moreinfos')  
    

    class Meta:
        model = User
        fields = ['id', 'username', 'moreinfo']


