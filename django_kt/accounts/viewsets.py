from rest_framework import viewsets

from django_kt.accounts.models import User


class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(delete_flag=False)
    serializer_class = None
