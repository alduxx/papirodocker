from django.http import HttpResponse
from django.shortcuts import render

from .models import Api, Service, ParameterGroup
from .forms import ParameterForm, ServiceForm, ApiForm

def index(request):
    api_list = Api.objects.order_by('name')
    context = {'api_list': api_list}
    return render(request, 'papiro/index.html', context)

def list_services(request, api_id):
    api = Api.objects.get(pk=api_id)
    service_list = Service.objects.filter(api=api).order_by('name')
    context = {'api': api, 'service_list':service_list}
    return render(request, 'papiro/services.html', context)

def service_detail(request, service_id):
    service = Service.objects.get(pk=service_id)
    parameter_groups = ParameterGroup.objects.filter(service=service).order_by('type')
    context = {'service': service, 'parameter_groups': parameter_groups}
    return render(request, 'papiro/service_detail.html', context)

def popup_add_parameter(request, service_id, parameter_group_id):
    if request.method == "POST":
        form = ParameterForm(request.POST)
        if form.is_valid():
            parameter = form.save(commit=False)
            parameter.save()
            return HttpResponse('<script type="text/javascript">window.opener.location.reload();window.close();</script>')
    else:
        form = ParameterForm()

        service = Service.objects.get(pk=service_id)
        parameter_group = ParameterGroup.objects.get(pk=parameter_group_id)
        context = {'service': service, 'parameter_group': parameter_group, 'form': form}
        return render(request, 'papiro/popup_new_parameter.html', context)


def popup_add_service(request, api_id):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()
            p_request = ParameterGroup(service=service, type="000")
            p_request.save()
            return HttpResponse(f'<script type="text/javascript">window.opener.location.href = "/api/service/{service.id}/";window.close();</script>')
    else:
        form = ServiceForm()

        api = Api.objects.get(pk=api_id)
        context = {'api': api, 'form': form}
        return render(request, 'papiro/popup_new_service.html', context)


def popup_add_api(request):
    if request.method == "POST":
        form = ApiForm(request.POST)
        if form.is_valid():
            api = form.save(commit=False)
            api.save()
            return HttpResponse(f'<script type="text/javascript">window.opener.location.href = "/api/{api.id}/services/";window.close();</script>')
    else:
        form = ApiForm()

        context = {'form': form}
        return render(request, 'papiro/popup_new_api.html', context)
