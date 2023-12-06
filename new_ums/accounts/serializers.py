from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','first_name','last_name','is_manager','is_executive']

#nested serializer for manager and executive extended from Userserializer
class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Manager
        fields = ['user', 'created_at']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        manager, created = Manager.objects.update_or_create(user=user, **validated_data)
        return manager

class ExecutiveSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Executive
        fields = ['user', 'created_at']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        executive, created = Executive.objects.update_or_create(user=user, **validated_data)
        return executive
    
#a new user and a new manager/executive are created, or an existing user and manager are updated,
# based on the validated data