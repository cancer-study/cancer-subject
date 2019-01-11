from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    ModelAdminNextUrlRedirectMixin, ModelAdminReplaceLabelTextMixin)
from edc_model_admin.model_admin_audit_fields_mixin import (
    audit_fields, audit_fieldset_tuple)

from ..admin_site import cancer_subject_admin
from ..forms import SubjectScreeningForm
from ..models import SubjectScreening


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(SubjectScreening, site=cancer_subject_admin)
class SubjectScreeningAdmin(ModelAdminMixin, FieldsetsModelAdminMixin,
                               admin.ModelAdmin):

    form = SubjectScreeningForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'subject_identifier',
                'has_diagnosis',
                'enrollment_site',
            )}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier',)

    radio_fields = {
        'has_diagnosis': admin.VERTICAL,
        'enrollment_site': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)