from django.contrib import admin

from ..models import OncologyTreatmentRecord, OTRChemo, OTRRadiation, OTRSurgical
from ..forms import OncologyTreatmentRecordForm, OTRChemoForm, OTRRadiationForm, OTRSurgicalForm
from cancer_subject.admin_site import cancer_subject_admin
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(OncologyTreatmentRecord, site=cancer_subject_admin)
class OncologyTreatmentRecordAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OncologyTreatmentRecordForm
    fields = (
        "subject_visit",
        "chemo_received",
        "radiation_received",
        "surgical_therapy",
        "comments")
    radio_fields = {
        "chemo_received": admin.VERTICAL,
        "radiation_received": admin.VERTICAL,
        "surgical_therapy": admin.VERTICAL}
    instructions = [("Note to Interviewer: If any of the answers below"
                     " are yes, make arrangements to obtain records or"
                     " review records over the phone")]


# class ChemoMedRecordInlineAdmin(BaseTabularInline):
#     model = ChemoMedRecord


@admin.register(OTRChemo, site=cancer_subject_admin)
class OTRChemoAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OTRChemoForm
#     inlines = [ChemoMedRecordInlineAdmin, ]
    fields = (
        "subject_visit",
        "chemo_intent",
        "chemo_delays",
        "why_delayed",
        "why_delayed_other",
        "chemo_reduced",
        "why_reduced",
        "why_reduced_other")
    radio_fields = {
        "chemo_intent": admin.VERTICAL,
        "chemo_delays": admin.VERTICAL,
        "why_delayed": admin.VERTICAL,
        "chemo_reduced": admin.VERTICAL,
        "why_reduced": admin.VERTICAL}


@admin.register(OTRRadiation, site=cancer_subject_admin)
class OTRRadiationAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OTRRadiationForm
    fields = (
        "subject_visit",
        "radiation_details",
    )
    radio_fields = {
        "radiation_details": admin.VERTICAL,
    }
    instructions = [("Review the recorded cancer type and stage information recorded and"
                      " consider updating 'Cancer Diagnosis' form accordingly.")]


@admin.register(OTRSurgical, site=cancer_subject_admin)
class OTRSurgicalAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OTRSurgicalForm
    fields = (
        "subject_visit",
        "operation_performed",
        "date_operation")
