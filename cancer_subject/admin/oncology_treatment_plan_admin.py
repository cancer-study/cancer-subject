from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from .modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..models import OncologyTreatmentPlan, ChemoMedPlan
from ..forms import OncologyTreatmentPlanForm


class ChemoMedPlanInlineAdmin(TabularInlineMixin, admin.TabularInline):
    exclude = ('dose_category',)
    model = ChemoMedPlan

# OncologyTreatmentPlan


@admin.register(OncologyTreatmentPlan, site=cancer_subject_admin)
class OncologyTreatmentPlanAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OncologyTreatmentPlanForm
    inlines = [ChemoMedPlanInlineAdmin, ]
    fields = (
        "subject_visit",
        "treatment_goal",
        "treatment_plan",
        "chemotherapy",
        "chemo_intent",
        "radiation_plan",
        #         "radiation_treatments",
        "surgical_plan",
        "planned_operation",
        "comments")
    radio_fields = {
        "treatment_goal": admin.VERTICAL,
        "treatment_plan": admin.VERTICAL,
        "chemotherapy": admin.VERTICAL,
        "chemo_intent": admin.VERTICAL,
        "radiation_plan": admin.VERTICAL,
        "surgical_plan": admin.VERTICAL}
