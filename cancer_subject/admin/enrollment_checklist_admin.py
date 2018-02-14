from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from edc_model_admin import audit_fieldset_tuple
# from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fields

from cancer_subject.admin_site import cancer_subject_admin

from ..forms import EnrollmentChecklistForm
from ..models import EnrollmentChecklist


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    #date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(EnrollmentChecklist, site=cancer_subject_admin)
class EnrollmentChecklistAdmin(ModelAdminMixin,
                               FieldsetsModelAdminMixin, admin.ModelAdmin):

    form = EnrollmentChecklistForm

    fieldsets = (
        (None, {
            'fields': (
                "subject_identifier",
                "has_diagnosis",
                'enrollment_site',
            )}),
        audit_fieldset_tuple)

#     readonly_fields = ('subject_identifier',) + audit_fields
    readonly_fields = ('subject_identifier',)

    radio_fields = {
        "has_diagnosis": admin.VERTICAL,
        "enrollment_site": admin.VERTICAL, }
