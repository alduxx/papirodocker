from django.contrib import admin

from .models import Api, Service, Parameter, ParameterGroup, TagSignature

class ParameterGroupTabularInline(admin.TabularInline):
    model = ParameterGroup

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = [ParameterGroupTabularInline]
    list_display = ('name', 'description', 'tag', 'http_method')
    class Meta:
        model = Service

class ParameterTabularInline(admin.TabularInline):
    model = Parameter

"""
@admin.register(ParameterGroup)
class ParameterGroupAdmin(admin.ModelAdmin):
    inlines = [ParameterTabularInline]
    #list_display = ('name', 'description', 'http_method')
    class Meta:
        model = ParameterGroup
    """

admin.site.register(Api)
# admin.site.register(Service, ServiceAdmin)
admin.site.register(ParameterGroup)
admin.site.register(Parameter)
admin.site.register(TagSignature)
