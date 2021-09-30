from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from .models import Users, Houses


class HousesSerializer(ModelSerializer):
    """This serializer for Houses-model"""

    class Meta:
        model = Houses
        fields = "__all__"        


class UsersSerializer(ModelSerializer):
    """This serializer for users-model"""
    
    own_houses_id = PrimaryKeyRelatedField(source='houses_set', many=True, read_only=True)
    class Meta:
        model = Users
        fields = ['name', 'salary', 'date', 'own_houses_id']
