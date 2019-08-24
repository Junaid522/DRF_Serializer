from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from core.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):

    query = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    query = Group.objects.all()
    serializer_class = GroupSerializer