#application assignment_api URLS file

from django.urls import path
from . import views

urlpatterns = [
	path("assignment_api/", views.user_details_list_create.as_view(), name="assignment_api_view_create"),
    path("assignment_api/<int:pk>/", views.user_details_retrieve_update_destroy.as_view(),name="update"),

]
