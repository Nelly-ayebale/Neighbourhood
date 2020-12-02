from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers

# Create your views here.
def index(request):
    return render(request,'hoods/home.html')

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

