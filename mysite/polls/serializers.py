import email
from django.forms import CharField
from rest_framework import serializers

from .models import *


from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MediaSerialzer(serializers.ModelSerializer):
    

    class Meta:
            model = MediaPeofile
            fields = ('image',)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    
    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email',)
    
    
    
        def validate(self, attrs):
            if attrs['password'] != attrs['password2']:
                raise serializers.ValidationError({"password": "Password fields didn't match."})

            return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user
        
        
class UserCreatSerializer(serializers.ModelSerializer):
        profile=MediaSerialzer()
        class Meta:
            
            model = User
            fields = ('username','email','profile')
            
            def update(self, instance, validated_data):
        
                instance.set_password(validated_data['username'],validated_data['email'],validated_data['profile'])
                instance.save()

                return instance
            
            
                
class UserProfileSerializer(serializers.ModelSerializer):
    media=MediaSerialzer()
    class Meta:
    
        model=User
        
        fields=('username','email','media')
        
        
            
class UserCreatSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        
        model=User
        
        fields=('username','email',)