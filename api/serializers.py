from models import *
from rest_framework_mongoengine.serializers import DocumentSerializer

class UserSerializer(DocumentSerializer):
    class Meta:
        model = User
        fields = ('name', 'username', 'email')
