from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import UserSerializer
from .service import CustomUserService



class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListUserProfileView(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class DeleteUserProfileView(generics.DestroyAPIView):
    queryset=CustomUserService.get_all_objects()
    print(queryset)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    

    
   
    
    