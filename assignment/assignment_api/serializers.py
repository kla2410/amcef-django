from rest_framework import serializers
from .models import user_details
from .models import user_content

class user_details_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ['id', 'userId', 'title', 'body']

class user_content_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_content
        fields = ['id', 'userId', 'title', 'body']