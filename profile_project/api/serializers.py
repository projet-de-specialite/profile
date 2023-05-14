from django.contrib.auth.models import User, Group
from rest_framework import serializers
from profile_project.api.models import Profile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'birth_date', 'created_on', 'id', 'name', 'user_id', 'website']

