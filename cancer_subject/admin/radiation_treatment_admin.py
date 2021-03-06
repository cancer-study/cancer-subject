from django.contrib import admin
from edc_model_admin import TabularInlineMixin

from ..admin_site import cancer_subject_admin
from ..forms import RadiationTreatmentForm
from ..models import RadiationTreatment, RadiationTreatmentRecord
from .modeladmin_mixins import CrfModelAdminMixin


class RadiationTreatmentRecordInlineAdmin(TabularInlineMixin,
                                          admin.TabularInline):
    model = RadiationTreatmentRecord
    extra = 1


@admin.register(RadiationTreatment, site=cancer_subject_admin)
class RadiationTreatmentAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = RadiationTreatmentForm
    inlines = [RadiationTreatmentRecordInlineAdmin, ]
    fields = (
        "subject_visit",
        "treatment_start_date",
        "treatment_end_date",
        "tumour_stages",
        "lymph_stages",
        "metastasis_stages",
        "overall_stages",
        "stage_modifier",
        "treatment_itent",
        "treatment_relationship",
        "side_effects",
        "side_effects_other",
        "response",
        "response_other",
        "any_missed_doses",
        "if_doses_missed",
        "if_doses_missed_other",
        "any_doses_delayed",
        "if_doses_delayed",
        "if_doses_delayed_other",
        "first_course_radiation",
        "comments",)
    radio_fields = {
        "tumour_stages": admin.VERTICAL,
        "lymph_stages": admin.VERTICAL,
        "metastasis_stages": admin.VERTICAL,
        "overall_stages": admin.VERTICAL,
        "stage_modifier": admin.VERTICAL,
        "treatment_itent": admin.VERTICAL,
        "treatment_relationship": admin.VERTICAL,
        # "side_effects": admin.VERTICAL,
        "response": admin.VERTICAL,
        "any_missed_doses": admin.VERTICAL,
        "if_doses_missed": admin.VERTICAL,
        "any_doses_delayed": admin.VERTICAL,
        "if_doses_delayed": admin.VERTICAL,
        "first_course_radiation": admin.VERTICAL, }
    filter_horizontal = ('side_effects',)
