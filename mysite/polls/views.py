from django.shortcuts import render


from urllib import request
from django.shortcuts import get_object_or_404

from .models import *
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,CreateAPIView,RetrieveUpdateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from .paginations import * 
from rest_framework import status


class SignUp(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    

class Profile(RetrieveUpdateAPIView):
    
    queryset = User.objects.all()
    lookup_field = 'username'
    def get_serializer_class(self):
        
        if self.request.method=='GET':
            
            return UserProfileSerializer

        else:
            return UserCreatSerializer
        
        
# class SetProfile(RetrieveAPIView):
    