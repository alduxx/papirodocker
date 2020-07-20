from django.urls import path, include

from . import views, rest_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:api_id>/services/', views.list_services, name='list_services'),
    path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('service/<int:service_id>/parameter_group/<int:parameter_group_id>/add/parameter/', views.popup_add_parameter, name='popup_add_parameter'),
    path('<int:api_id>/services/add/service/', views.popup_add_service, name='popup_add_service'),
    path('add/', views.popup_add_api, name='popup_add_api'),
    path('rest/', include(rest_urls)),
]