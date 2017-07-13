from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    FormAsJSONModelAdminMixin, ModelAdminRedirectOnDeleteMixin)
from edc_base.fieldsets import FieldsetsModelAdminMixin
from edc_visit_tracking.modeladmin_mixins import (
    CrfModelAdminMixin as VisitTrackingCrfModelAdminMixin)


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'


class CrfModelAdminMixin(VisitTrackingCrfModelAdminMixin,
                         ModelAdminRedirectOnDeleteMixin,
                         ModelAdminMixin,
                         FieldsetsModelAdminMixin,
                         FormAsJSONModelAdminMixin,
                         admin.ModelAdmin):

    post_url_on_delete_name = 'ambition_subject:dashboard_url'
    instructions = (
        'Please complete the questions below. Required questions are in bold. '
        'When all required questions are complete click SAVE. '
        'Based on your responses, additional questions may be '
        'required or some answers may need to be corrected.')

    def post_url_on_delete_kwargs(self, request, obj):
        return dict(
            subject_identifier=obj.subject_identifier,
            appointment=str(obj.subject_visit.appointment.id))

    def view_on_site(self, obj):
        try:
            return reverse(
                'ambition_subject:dashboard_url', kwargs=dict(
                    subject_identifier=obj.subject_visit.appointment.subject_identifier))
        except NoReverseMatch:
            return super().view_on_site(obj)
