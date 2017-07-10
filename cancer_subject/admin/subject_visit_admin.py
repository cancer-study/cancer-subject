from django.contrib import admin

from edc.subject.appointment.admin import BaseAppointmentModelAdmin

from ...cancer_lab.models import SubjectRequisition
from ..models import SubjectVisit
from ..forms import SubjectVisitForm


class SubjectVisitAdmin(BaseAppointmentModelAdmin):

    form = SubjectVisitForm
    visit_model_instance_field = 'subject_visit'
    requisition_model = SubjectRequisition
    dashboard_type = 'subject'
    date_heirarchy = 'report_datetime'
    list_display = (
        'appointment',
        'report_datetime',
        'reason',
        "info_source",
        'created',
        'user_created',)
    list_filter = (
        'report_datetime',
        'reason',
        'appointment__appt_status',
        'appointment__visit_definition__code',)
    search_fields = (
        'appointment__registered_subject__subject_identifier',
        'appointment__registered_subject__registration_identifier',
        'appointment__registered_subject__first_name',
        'appointment__registered_subject__identity',)
    fields = (
        "appointment",
        "report_datetime",
        "info_source",
        "info_source_other",
        "reason",
        "reason_unscheduled",
        "reason_missed",
        "comments")
    radio_fields = {
        "reason_unscheduled": admin.VERTICAL}
admin.site.register(SubjectVisit, SubjectVisitAdmin)
