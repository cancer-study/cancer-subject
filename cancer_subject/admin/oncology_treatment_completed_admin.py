from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..forms import OncologyTreatmentCompletedForm
from ..models import OncologyTreatmentCompleted
from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import cancer_subject_admin


@admin.register(OncologyTreatmentCompleted, site=cancer_subject_admin)
class OncologyTreatmentCompletedAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OncologyTreatmentCompletedForm

    fieldsets = (
        (None, {
            'fields': (
                'patient_had_chemo',
                'patient_had_radiation',
                'patient_had_surgery',
                'treatment_detail',
                'patient_follow_up',
                'patient_follow_up_other',
                'next_followup',
            )}),
        audit_fieldset_tuple
    )
    radio_fields = {
        'patient_had_chemo': admin.VERTICAL,
        'patient_had_radiation': admin.VERTICAL,
        'patient_had_surgery': admin.VERTICAL,
        'patient_follow_up': admin.VERTICAL
    }
