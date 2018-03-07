from django.contrib import admin

from .modeladmin_mixins import ModelAdminMixin


class LabResultAdminMixin(ModelAdminMixin, admin.ModelAdmin):
    pass
