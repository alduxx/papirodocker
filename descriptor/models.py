from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Api(models.Model):
    name = models.CharField(_('name'), max_length=60, unique=True)
    description = models.TextField(_('description'), blank=True)
    enabled = models.BooleanField(_('enabled'), default=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    SERVICE_STATUS = [
        ('ST', _('under study').capitalize()),
        ('DV', _('under development').capitalize()),
        ('HM', _('under test').capitalize()),
        ('DP', _('deployed').capitalize()),
    ]

    HTTP_METHODS = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('PATCH', 'PATCH'),
    ]

    api = models.ForeignKey(Api, on_delete=models.CASCADE)
    name = models.CharField(_('name'), max_length=120)
    description = models.TextField(_('description'), blank=True, default="")
    status = models.CharField(max_length=2, choices=SERVICE_STATUS, blank=False, null=False)
    iib_service_number = models.PositiveIntegerField(_('iib service number'), blank=True, null=True, help_text=_('Insert IIB Service Number if already available. '))
    iib_service_version_number = models.PositiveSmallIntegerField(_('iib service version number'), blank=True, null=True)
    endpoint_uri = models.CharField(_('endpoint uri'), max_length=200, blank=True, default="")
    http_method = models.CharField(_('method'), max_length=6, blank=False, null=False, choices=HTTP_METHODS)
    enabled = models.BooleanField(_('enabled'), default=True)
    tag = models.PositiveSmallIntegerField(_('tag'), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')


class ParameterGroup(models.Model):
    PARAMETER_GROUP_TYPE = [
        ('000', _('request').capitalize()),
        ('200', _('response 200 - ok').capitalize()),
        ('400', _('response 400 - error').capitalize()),
        ('403', _('response 403 - forbidden').capitalize()),
        ('500', _('response 500 - server error').capitalize()),
    ]

    type = models.CharField(_('parameter type'), max_length=3, blank=False, null=False, choices=PARAMETER_GROUP_TYPE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        #return f"{self.service.name} - {self.get_type_display()}"
        return self.service.name + "-" + self.get_type_display()

    class Meta:
        verbose_name = _('parameter group')
        verbose_name_plural = _('parameter groups')


class Parameter(models.Model):
    FORMATS = [
        ('AN', _('alphanumeric').capitalize()),
        ('NB', _('number').capitalize()),
        ('AR', _('array').capitalize()),
        ('OB', _('object').capitalize()),
    ]

    name = models.CharField(_('name'), max_length=40)
    format = models.CharField(_('format'), max_length=2, blank=False, null=False, choices=FORMATS)
    size = models.CharField(_('size'), max_length=20)
    required = models.BooleanField(_('required'), default=True)
    domain_rules = models.CharField(_('domain rules'), max_length=120, blank=True, default="")
    parameter_group = models.ForeignKey(ParameterGroup, on_delete=models.CASCADE, related_name='parameters')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('parameter')
        verbose_name_plural = _('parameter')


class TagSignature(models.Model):
    first_signer = models.ForeignKey(User, related_name='First_signer', on_delete=models.CASCADE, null=False)
    second_signer = models.ForeignKey(User, related_name='Second_signer', on_delete=models.CASCADE, null=True, default=None)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    signed_at = models.DateTimeField(auto_now_add=True)

    def is_closed(self):
        return (self.first_signer is not None) and (self.second_signer is not None)

    def __str__(self):
        if self.first_signer and self.second_signer:
            return f"{_('Signed by')} {self.first_signer.username}  {_(' and ')} {self.second_signer.username} + \
                   {_(' at ')} {self.signed_at}"
        else:
            return f"{_('Signed by')} {self.first_signer.username} {_(' at ')} {self.signed_at}"

    class Meta:
        verbose_name = _('parameter')
        verbose_name_plural = _('parameter')