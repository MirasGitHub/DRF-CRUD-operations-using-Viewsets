from django.contrib.auth.models import User
from rest_framework import serializers

from posts.models import Post


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'slug',
            'user'
        ]


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=150, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

        read_only_fields = ['token']
