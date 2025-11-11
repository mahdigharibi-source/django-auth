from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.response import Response


class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.save()
        return user

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        if not username:
            raise serializers.ValidationError('Username is required')
        if not password:
            raise serializers.ValidationError('Password is required')
        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError('Invalid username or password')
        attrs['user']= user
        return attrs

