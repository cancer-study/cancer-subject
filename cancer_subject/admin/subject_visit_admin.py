from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch

from edc_base.modeladmin_mixins import audit_fieldset_tuple, audit_fields
from edc_visit_schedule.admin import (
    visit_schedule_fieldset_tuple, visit_schedule_fields)
from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin_site import ambition_subject_admin
from ..forms import SubjectVisitForm
from ..models import SubjectVisit, SubjectRequisition
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectVisit, site=ambition_subject_admin)
class SubjectVisitAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = SubjectVisitForm

    requisition_model = SubjectRequisition

    fieldsets = (
        (None, {
            'fields': [
                'appointment',
                'report_datetime',
                'comments']}),
        visit_schedule_fieldset_tuple,
        audit_fieldset_tuple)

    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        'info_source',
        'created',
        'user_created',
    )

    list_filter = (
        'report_datetime',
        'reason',
        'appointment__appt_status',
        'appointment__visit_code',
    )

    search_fields = (
        'appointment__subject_identifier',
        'appointment__registered_subject__registration_identifier',
        'appointment__registered_subject__first_name',
        'appointment__registered_subject__identity',
    )

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj) + audit_fields
                + visit_schedule_fields)

    def view_on_site(self, obj):
        try:
            return reverse(
                'ambition_subject:dashboard_url', kwargs=dict(
                    subject_identifier=obj.subject_identifier,
                    appointment=str(obj.appointment.id)))
        except NoReverseMatch as e:
            print(e)
            return super().view_on_site(obj)
