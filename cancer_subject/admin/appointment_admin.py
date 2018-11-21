from django.contrib import admin
from edc_appointment.models.appointment import Appointment
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from cancer_subject.admin_site import cancer_subject_admin

from ..forms import AppointmentForm
from .modeladmin_mixins import ModelAdminMixin


@admin.register(Appointment, site=cancer_subject_admin)
class AppointmentAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = AppointmentForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'appt_datetime',
                'appt_type',
                'appt_status',
                'appt_reason',
                'comment',
            ]}),
        audit_fieldset_tuple)

    list_display = (
        'subject_identifier', 'visit_code', 'appt_datetime', 'appt_status')

    list_filter = (
        'visit_code', 'appt_datetime', 'appt_status', 'appt_type')

    search_fields = ('subject_identifier', )

    radio_fields = {
        'appt_status': admin.VERTICAL,
        'appt_type': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + ('subject_identifier',))
