from rest_framework import serializers
from .models import Transaction
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'description','amount', 'date', 'type']
        extra_kwargs = {"user": {"read_only": True}}

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  # Assign the logged-in user
        return super().create(validated_data)


