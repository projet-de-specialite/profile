from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from profile_project.api.serializers import UserSerializer, GroupSerializer
from rest_framework_swagger.views import get_swagger_view
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

