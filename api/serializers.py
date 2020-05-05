from django.contrib.auth.models import User, Group
from rest_framework import serializers
from comex.models import *


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['description', 'name', 'networkType', 'managed', 'status']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
