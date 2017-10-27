from django.contrib import admin
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.fieldsets import FieldsetsModelAdminMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin)
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import cancer_subject_admin
from ..forms.subject_eligibility_form import SubjectEligibilityForm

from ..models import SubjectEligibility


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


@admin.register(SubjectEligibility, site=cancer_subject_admin)
class SubjectEligibilityAdmin(ModelAdminMixin, FieldsetsModelAdminMixin, admin.ModelAdmin):

    form = SubjectEligibilityForm

    instructions = ['This form is a tool to assist the Interviewer to confirm the '
                    'Eligibility status of the subject. After entering the required items, click SAVE.']

    fieldsets = (
        (None, {
            'fields': (
                #                 'report_datetime',
                #                 'first_name',
                #                 'initials',
                #                 'gender',
                "cancer_status",
                'enrollment_site',
                #                 'age_in_years',
                #                 'has_identity',
                #                 "guardian",
                #                 "citizen",
                #                 "legal_marriage",
                #                 "marriage_certificate",
                #                 "literacy",
                #                 'inability_to_participate'
            )}),
        audit_fieldset_tuple)

    list_display = (
        'report_datetime', 'gender')

    radio_fields = {
        'has_identity': admin.VERTICAL,
        "gender": admin.VERTICAL,
        "citizen": admin.VERTICAL,
        "legal_marriage": admin.VERTICAL,
        "marriage_certificate": admin.VERTICAL,
        "literacy": admin.VERTICAL,
        "guardian": admin.VERTICAL,
        "inability_to_participate": admin.VERTICAL,
        "cancer_status": admin.VERTICAL,
        "enrollment_site": admin.VERTICAL,
    }

    search_fields = (
        'first_name',
        'initials',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj))
