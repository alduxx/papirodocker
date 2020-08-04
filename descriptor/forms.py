from django.forms import ModelForm
from .models import Parameter, Service, Api

class ApiForm(ModelForm):
     class Meta:
         model = Api
         fields = ['name', 'description']

class ParameterForm(ModelForm):
     class Meta:
         model = Parameter
         fields = ['name', 'format', 'size', 'required', 'domain_rules', 'parameter_group', 'parameter_parent']

class ServiceForm(ModelForm):
     class Meta:
         model = Service
         fields = ['api', 'name', 'description', 'status', 'iib_service_number',
                  'iib_service_version_number', 'endpoint_uri', 'http_method', ]
