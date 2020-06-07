from rest_framework import viewsets
from accounts.api.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
