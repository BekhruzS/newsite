from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

class UserListCreate(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
