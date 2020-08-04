import itertools
import pytz

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import ParameterForm, ServiceForm, ApiForm
from .models import Api, Service, Parameter, ParameterGroup, TagSignature

SNAPSHOT = 0 # const

#@login_required
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
    api = Api.objects.get(pk=api_id)
    service_list = Service.objects.filter(api=api, tag=SNAPSHOT).order_by('name')
    context = {'api': api, 'service_list':service_list}
    return render(request, 'papiro/services.html', context)


def service_detail_by_name(request, api_id, service_name):
    """
    Render service detail by api_id and service name with tag == SNAPSHOT (0) 
    """

    return service_detail_by_name_and_tag(request, api_id, service_name, SNAPSHOT)


def service_detail_by_name_and_tag(request, api_id, service_name, tag):
    """
    Render service detail by api_id and service name and tag
    """

    api = Api.objects.get(pk=api_id)

    all_services_with_name = Service.objects.filter(api=api, name=service_name).order_by('tag')

    # get working service with tag 0 (not a closed service)
    service = Service.objects.get(api=api, name=service_name, tag=tag)

    # try to find tag signature, otherwise returns none
    tag_signature = None
    try:
        tag_signature = TagSignature.objects.get(service=service)
    except TagSignature.DoesNotExist:
        pass
    
    # Checks if there is a pending tag for any version of that service
    pending_tag = None
    for _service in all_services_with_name:
        for _tag in _service.tag_signatures.all():
            if not _tag.is_closed() and _service.tag != SNAPSHOT:
                pending_tag = _tag
                break

    custom_counter = TemplateIterator()

    # pass all_services_with_name to create dropdown with tags
    context = {'service': service,
               'all_services': all_services_with_name,
               'mycounter': custom_counter,
               'tag_signature': tag_signature,
               'pending_tag': pending_tag}

    return render(request, 'papiro/service_details.html', context)


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

        tag_signature = TagSignature(service=service,
                                     first_signer=request.user, 
                                     first_signature_signed_at=timezone.now())
        tag_signature.save()

        return HttpResponse(service.tag)
    else:
        return HttpResponse('error')

def confirm_new_tag(request, service_id):
    """
    Confirms new tag from SNAPSHOT version
    Second signature
    """
    if request.method == "POST":
        service = Service.objects.get(pk=service_id)
        tag_signature = TagSignature.objects.get(service=service)
        tag_signature.second_signer = request.user
        tag_signature.second_signature_signed_at = timezone.now()
        tag_signature.save()

        return HttpResponse(service.tag)
    else:
        return HttpResponse('error')


def popup_add_parameter_with_parent(request, service_id, parameter_group_id, parent_id):
    if request.method == "POST":
        form = ParameterForm(request.POST)
        if form.is_valid():
            parameter = form.save(commit=False)
            parameter.save()
            return HttpResponse('<script type="text/javascript">window.opener.location.reload();window.close();</script>')
    else:
        form = ParameterForm()

        service = Service.objects.get(pk=service_id)

        context = {'service': service, 'parameter_group_id': parameter_group_id, 'parent_id': parent_id, 'form': form}
        return render(request, 'papiro/popup_new_parameter.html', context)


def popup_add_parameter(request, service_id, parameter_group_id):
    return popup_add_parameter_with_parent(request, service_id, parameter_group_id, None)


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

            return HttpResponse(f'<script type="text/javascript">window.opener.location.href = window.opener.location.href;window.close();</script>')
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


def force_auth(request, username):
    user = User.objects.get(username=username)
    login(request, user)
    # return index(request)
    return redirect('/api/')


class TemplateIterator(itertools.count):
    """
    Used to create custom loop counter.
    See function service_detail_by_name_and_tag.
    """
    def next(self):
        return next(self)