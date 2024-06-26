from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ("firstname","lastname","email","password","age","contact","address","gender","height","weight")