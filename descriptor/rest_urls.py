from django.urls import path, include

from . import rest_views

urlpatterns = [
    path('apis/', rest_views.api_list, name='api_list'),
    path('apis/<int:api_id>/', rest_views.api_detail, name='api_detail'),
]
