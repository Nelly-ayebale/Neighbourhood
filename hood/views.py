from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Neighbourhood,Profile,Business
from .serializers import NeighbourhoodSerializer,ProfileSerializer,BusinessSerializer

# Create your views here.
def index(request):
    return render(request,'hoods/home.html')

