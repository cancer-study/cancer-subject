from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.fieldsets import FieldsetsModelAdminMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from cancer_subject.admin_site import cancer_subject_admin

from ..forms import EnrollmentChecklistForm
from ..models import EnrollmentChecklist


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(EnrollmentChecklist, site=cancer_subject_admin)
class EnrollmentChecklistAdmin(ModelAdminMixin,
                               FieldsetsModelAdminMixin, admin.ModelAdmin):

    form = EnrollmentChecklistForm

    fieldsets = (
        (None, {
            'fields': (
                "has_diagnosis",
                'enrollment_site',
            )}),
        audit_fieldset_tuple)

    radio_fields = {
        "has_diagnosis": admin.VERTICAL,
        "enrollment_site": admin.VERTICAL, }
