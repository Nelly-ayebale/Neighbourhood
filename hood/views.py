from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from .serializers import NeighbourhoodSerializer
from rest_framework import viewsets
from .models import Neighbourhood
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

    