from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple



from ..admin_site import cancer_subject_admin
from ..forms import SubjectLocatorForm
from ..models import SubjectLocator
from .modeladmin_mixins import ModelAdminMixin
from edc_locator.fieldsets import subject_contacts_fieldset,\
    work_contacts_fieldset, indirect_contacts_fieldset
from ..fieldsets import other_indirect_contacts_fieldset



@admin.register(SubjectLocator, site=cancer_subject_admin)
class SubjectLocatorAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectLocatorForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'date_signed',
                'local_clinic',
                'home_village',
            )}),
        subject_contacts_fieldset,
        work_contacts_fieldset,
        indirect_contacts_fieldset,
        other_indirect_contacts_fieldset,
        audit_fieldset_tuple,
    )

    radio_fields = {
        'may_visit_home': admin.VERTICAL,
        'may_call': admin.VERTICAL,
        'may_sms': admin.VERTICAL,
        'may_call_work': admin.VERTICAL,
        'may_contact_indirectly': admin.VERTICAL}

    list_filter = (
        'may_visit_home',
        'may_call',
        'may_sms',
        'may_call_work',
        'may_contact_indirectly')

    list_display = (
        'subject_identifier',
#         'dashboard',
        'visit_home',
        'call',
        'sms',
        'call_work',
        'contact_indirectly')

    search_fields = ('subject_identifier', )
