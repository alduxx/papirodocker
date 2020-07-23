from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Api, Service, Parameter, ParameterGroup
from .forms import ParameterForm, ServiceForm, ApiForm

@login_required
def index(request):
    """
    View for index page where it lists all api projects
    """
    api_list = Api.objects.order_by('name')
    context = {'api_list': api_list}
    return render(request, 'papiro/index.html', context)


def list_services(request, api_id):
    """
    Show list of services from api project.
    Only shows SNAPSHOT versions
    """
    SNAPSHOT = 0
    api = Api.objects.get(pk=api_id)
    service_list = Service.objects.filter(api=api, tag=SNAPSHOT).order_by('name')
    context = {'api': api, 'service_list':service_list}
    return render(request, 'papiro/services.html', context)


def service_detail_by_name(request, api_id, service_name):
    """
    Render service detail by api_id and service name
    """
    all_services_with_name = Service.objects.filter(name=service_name).order_by('tag')
    # get working service with tag 0 (not a closed service)
    service = all_services_with_name[0]
    parameter_groups = ParameterGroup.objects.filter(service=service).order_by('type')
    # pass all_services_with_name to create dropdown with tags
    context = {'service': service, 'all_services': all_services_with_name, 'parameter_groups': parameter_groups}
    return render(request, 'papiro/service_detail.html', context)


def service_detail_by_name_and_tag(request, api_id, service_name, tag):
    """
    Render service detail by api_id and service name and tag
    """
    all_services_with_name = Service.objects.filter(name=service_name).order_by('tag')
    # get working service with tag 0 (not a closed service)
    service = Service.objects.get(name=service_name, tag=tag)
    parameter_groups = ParameterGroup.objects.filter(service=service).order_by('type')
    # pass all_services_with_name to create dropdown with tags
    context = {'service': service, 'all_services': all_services_with_name, 'parameter_groups': parameter_groups}
    return render(request, 'papiro/service_detail.html', context)


def create_new_tag(request, service_id):
    """
    Creates new tag from SNAPSHOT version
    """
    if request.method == "POST":
        service = Service.objects.get(pk=service_id)

        last_version_service = Service.objects.filter(name=service.name).order_by('-tag')[0]

        parameter_groups = ParameterGroup.objects.filter(service=service) #saves for later

        service.pk = None # clones the service object
        service.tag = last_version_service.tag + 1
        service.save()

        for pgroup in parameter_groups:
            # clones parameter groups
            parameters = Parameter.objects.filter(parameter_group=pgroup) # saves up
            pgroup.pk = None
            pgroup.service = service
            pgroup.save()

            for param in parameters:
                param.pk = None
                param.parameter_group = pgroup
                param.save()

        return HttpResponse(service.tag)
    else:
        return HttpResponse('error')


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
    """
    Handles form for adding a new service
    """
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.save()

            for value, text in ParameterGroup.PARAMETER_GROUP_TYPE:
                # Adds all parameter groups to service
                new_pgroup = ParameterGroup(service=service, type=value)
                new_pgroup.save()

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
            return HttpResponse(f'<script type="text/javascript">window.opener.location.href = "/api/";window.close();</script>')
    else:
        form = ApiForm()

        context = {'form': form}
        return render(request, 'papiro/popup_new_api.html', context)
