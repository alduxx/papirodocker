from django.urls import path, include
from django.views.generic import TemplateView

from . import views, rest_urls

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:api_id>/services/', views.list_services, name='list_services'),
    # path('service/<int:service_id>/', views.service_detail, name='service_detail'),
    path('<int:api_id>/service/<slug:service_name>/', views.service_detail_by_name, name='service_detail_by_name'),
    path('<int:api_id>/service/<slug:service_name>/tag/<int:tag>', views.service_detail_by_name_and_tag, name='service_detail_by_name_and_tag'),
    path('service/<int:service_id>/parameter_group/<int:parameter_group_id>/add/parameter/', views.popup_add_parameter, name='popup_add_parameter'),
    path('service/<int:service_id>/parameter_group/<int:parameter_group_id>/add/parameter/with/parent/<int:parent_id>/', views.popup_add_parameter_with_parent, name='popup_add_parameter_with_parent'),
    path('<int:api_id>/services/add/service/', views.popup_add_service, name='popup_add_service'),
    path('add/', views.popup_add_api, name='popup_add_api'),

    path('service/<int:service_id>/tag/commit/', views.create_new_tag, name='create_new_tag'),
    path('service/<int:service_id>/tag/confirm/commit/', views.confirm_new_tag, name='confirm_new_tag'),

    path('user/<slug:username>/', views.force_auth, name='force_auth'),

    path('noservices/', TemplateView.as_view(template_name='papiro/noservices.html')),

    path('rest/', include(rest_urls)),
]
