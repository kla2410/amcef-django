from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import user_details
from .serializers import user_details_serializer
import requests
from django.http import JsonResponse
from django.views import View


class user_details_list_create(generics.ListCreateAPIView):
    queryset = user_details.objects.all()
    serializer_class = user_details_serializer

    def delete(self,request, *args, **kwargs):
        user_details.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class user_details_retrieve_update_destroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = user_details.objects.all()
    serializer_class = user_details_serializer
    lookup_field = "pk"

## contact api target at https://jsonplaceholder.typicode.com/posts

def external_api(id, userId, title, body):
    url = "https://jsonplaceholder.typicode.com/posts"
    ex_api_response = requests.get(url)
    ex_api_data = ex_api_response.json()
    return JsonResponse(ex_api_response)



