from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from .serializers import NeighbourhoodSerializer,BusinessSerializer,ProfileSerializer,HoodSerializer,JoinSerializer,PostSerializer
from rest_framework import viewsets
from .models import Neighbourhood,Business,Post,Join,Profile,Hood
from .permissions import IsAdminOrReadOnly

# Create your views here.
def index(request):
    return render(request,'hoods/home.html')

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class HoodSetView(viewsets.ModelViewSet):
    serializer_class = NeighbourhoodSerializer
    queryset = Neighbourhood.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class BusinessSetView(viewsets.ModelViewSet):
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class PostSetView(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdminOrReadOnly]

class ProfileSetView(viewsets.ViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class HoodListView(generics.ListAPIView):
    serializer_class = HoodSerializer
    queryset = Hood.objects.all()

class JoinSetView(viewsets.ModelViewSet):
    serializer_class = JoinSerializer
    queryset = Join.objects.all()