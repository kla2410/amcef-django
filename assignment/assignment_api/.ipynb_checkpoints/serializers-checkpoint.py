from rest_framework import serializers
from .models import user_details

class assigment_api_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_details
        fields = ['id', 'userid', 'title', 'body']