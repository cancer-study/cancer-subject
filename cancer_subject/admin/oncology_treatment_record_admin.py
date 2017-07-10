from django.contrib import admin

from edc.base.modeladmin.admin import BaseTabularInline

from .subject_visit_model_admin import SubjectVisitModelAdmin
from ..models import ChemoMedRecord, OncologyTreatmentRecord, OTRChemo, OTRRadiation, OTRSurgical
from ..forms import OncologyTreatmentRecordForm, OTRChemoForm, OTRRadiationForm, OTRSurgicalForm


# OncologyTreatmentRecord
class OncologyTreatmentRecordAdmin(SubjectVisitModelAdmin):

    form = OncologyTreatmentRecordForm
    fields = (
        "subject_visit",
#        "treatment_received",
        "chemo_received",
        "radiation_received",
        "surgical_therapy",
        "comments")
    radio_fields = {
#        "treatment_received": admin.VERTICAL,
        "chemo_received": admin.VERTICAL,
        "radiation_received": admin.VERTICAL,
        "surgical_therapy": admin.VERTICAL}
    instructions = [("Note to Interviewer: If any of the answers below"
                     " are yes, make arrangements to obtain records or"
                     " review records over the phone")]
admin.site.register(OncologyTreatmentRecord, OncologyTreatmentRecordAdmin)


class ChemoMedRecordInlineAdmin(BaseTabularInline):
    model = ChemoMedRecord


# OTRChemo
class OTRChemoAdmin(SubjectVisitModelAdmin):

    form = OTRChemoForm
    inlines = [ChemoMedRecordInlineAdmin, ]
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
admin.site.register(OTRChemo, OTRChemoAdmin)


# OTRRadiation
class OTRRadiationAdmin(SubjectVisitModelAdmin):

    form = OTRRadiationForm
    fields = (
        "subject_visit",
        "radiation_details",
#         "concomitant",
#         "amount_radiation"
    )
    radio_fields = {
        "radiation_details": admin.VERTICAL,
#         "concomitant": admin.VERTICAL
    }
    instructions = [("Review the recorded cancer type and stage information recorded and"
                      " consider updating 'Cancer Diagnosis' form accordingly.")]
admin.site.register(OTRRadiation, OTRRadiationAdmin)


#OTRSurgical
class OTRSurgicalAdmin(SubjectVisitModelAdmin):

    form = OTRSurgicalForm
    fields = (
        "subject_visit",
        "operation_performed",
        "date_operation")
admin.site.register(OTRSurgical, OTRSurgicalAdmin)
