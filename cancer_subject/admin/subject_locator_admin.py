from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import cancer_subject_admin

from ..forms import SubjectLocatorForm
from ..models import SubjectLocator
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectLocator, site=cancer_subject_admin)
class SubjectLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'mail_address',
                'home_visit_permission',
                'physical_address',
                'may_follow_up',
                'may_sms_follow_up',
                'subject_cell',
                'subject_cell_alt',
                'subject_phone',
                'subject_phone_alt',
                'may_contact_someone',
                'contact_name',
                'contact_rel',
                'contact_physical_address',
                'contact_cell',
                'alt_contact_cell_number',
                'contact_phone',
                'has_alt_contact',
                'alt_contact_name',
                'alt_contact_rel',
                'alt_contact_cell',
                'other_alt_contact_cell',
                'alt_contact_tel',
                'may_call_work',
                'subject_work_place',
                'subject_work_phone')}),
        audit_fieldset_tuple,
    )

    radio_fields = {
        'home_visit_permission': admin.VERTICAL,
        #         'may_follow_up': admin.VERTICAL,
        #         'may_sms_follow_up': admin.VERTICAL,
        'has_alt_contact': admin.VERTICAL,
        'may_call_work': admin.VERTICAL,
        #         'may_contact_someone': admin.VERTICAL,
    }

    list_filter = (
        #         'may_follow_up',
        #         'may_contact_someone',
        'may_call_work',
        'home_visit_permission')

    list_display = (
        'subject_identifier',
        'home_visit_permission',
        #         'may_follow_up',
        'has_alt_contact',
        'may_call_work',
        #         'may_contact_someone'
    )
