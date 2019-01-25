from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..forms import CurrentSymptomsForm
from ..models import CurrentSymptoms
from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import cancer_subject_admin


@admin.register(CurrentSymptoms, site=cancer_subject_admin)
class CurrentSymptomsAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = CurrentSymptomsForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'any_worry',
                'symptom_desc',
                'patient_own_remedy',
                'severity',
                'ra_advice',
                'outcome_update',
            )}),
        audit_fieldset_tuple
    )
    radio_fields = {
        'any_worry': admin.VERTICAL,
        'severity': admin.VERTICAL
    }
