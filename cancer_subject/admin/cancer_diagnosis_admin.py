from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..forms import CancerDiagnosisForm
from ..models import CancerDiagnosis
from .modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import cancer_subject_admin


@admin.register(CancerDiagnosis, site=cancer_subject_admin)
class CancerDiagnosisAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = CancerDiagnosisForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'subject_visit',
                "onco_number",
                "pathology_number",
                "pm_number",
                "diagnosis",
                "cancer_category",
                "symptom_prompt",
                "symptom_prompt_other",
                "symptom_first_noticed",
                "first_evaluation",
                "trad_evaluation",
                "date_diagnosed",
                "diagnosis_basis",
                "diagnosis_basis_other",
                "diagnosis_word",
                "cancer_site",
                "clinical_diagnosis",
                "tumour",
                "tumour_basis",
                "lymph_nodes",
                "lymph_basis",
                "metastasis",
                "metastasis_basis",
                "cancer_stage",
                "cancer_stage_modifier",
                "any_other_results",
                "paper_documents",
                "results_to_record",
                "results_to_record_other",)}),
        audit_fieldset_tuple
    )
    radio_fields = {
        "diagnosis": admin.VERTICAL,
        "cancer_category": admin.VERTICAL,
        "symptom_prompt": admin.VERTICAL,
        "diagnosis_basis": admin.VERTICAL,
        "tumour": admin.VERTICAL,
        "tumour_basis": admin.VERTICAL,
        "lymph_nodes": admin.VERTICAL,
        "lymph_basis": admin.VERTICAL,
        "metastasis": admin.VERTICAL,
        "metastasis_basis": admin.VERTICAL,
        "cancer_stage": admin.VERTICAL,
        "cancer_stage_modifier": admin.VERTICAL,
        "any_other_results": admin.VERTICAL}
    filter_horizontal = ('results_to_record',)
