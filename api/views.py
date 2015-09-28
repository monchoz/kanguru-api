from rest_framework_mongoengine.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *

class UserList(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
