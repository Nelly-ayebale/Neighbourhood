from rest_framework import serializers
from . import models
from .models import Neighbourhood,Business,Post,Join,Profile,Hood

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id','email', 'username','profile_photo','status','neighbourhood')

class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = '__all__'

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(max_length=None, use_url=True)
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'

class HoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hood
        fields = '__all__'

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = '__all__'