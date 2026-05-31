from rest_framework import serializers
from django.contrib.auth.models import User
from .models import News

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class NewsSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = News
        fields = ['id', 'title', 'summary', 'content', 'author', 'author_name', 'date_created']
        read_only_fields = ['author', 'date_created']

    def validate_content(self, value):
        if len(value) < 50:
            raise serializers.ValidationError("Минимум 50 символов.")
        return value