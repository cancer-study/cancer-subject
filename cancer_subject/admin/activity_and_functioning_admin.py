from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from .modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import ActivityAndFunctioningForm
from ..models import ActivityAndFunctioning


@admin.register(ActivityAndFunctioning, site=cancer_subject_admin)
class ActivityAndFunctioningAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = ActivityAndFunctioningForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'subject_visit',
                "health_rate",
                "health_problems",
                "difficulty_work",
                "bodily_pain",
                "energy",
                "health_probs_limit",
                "emotional_probs",
                "probs_from_work",
                "perform_status",
                "flu_symptoms",
                "symptom_specify",
                "housemates_count",
                "housemate_flu_symptoms",
                "housemates_with_flu_symptoms_count",
                "closest_health_facility",
                "contact_with_covid_suspect",
                "had_covid",
                "symp_dt",
                "pos_covid_test",
                "member_w_covid",
                "num_of_members",
                "membr_symp_dt")}),
        audit_fieldset_tuple
    )
    radio_fields = {
        "health_rate": admin.VERTICAL,
        "health_problems": admin.VERTICAL,
        "difficulty_work": admin.VERTICAL,
        "bodily_pain": admin.VERTICAL,
        "energy": admin.VERTICAL,
        "health_probs_limit": admin.VERTICAL,
        "emotional_probs": admin.VERTICAL,
        "probs_from_work": admin.VERTICAL,
        "perform_status": admin.VERTICAL,
        "flu_symptoms": admin.VERTICAL,
        "housemate_flu_symptoms": admin.VERTICAL,
        "contact_with_covid_suspect": admin.VERTICAL,
        "had_covid": admin.VERTICAL,
        "pos_covid_test": admin.VERTICAL,
        "member_w_covid": admin.VERTICAL, }

    filter_horizontal = ("symptom_specify",)
