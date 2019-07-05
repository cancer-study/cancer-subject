# from django.contrib import admin
# from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin
#
# from cancer_subject.admin.modeladmin_mixins import CrfModelAdminMixin
# from cancer_subject.admin_site import cancer_subject_admin
# from cancer_subject.forms.main import HaartMedRecordForm, ChemoMedPlanForm
# from cancer_subject.models.chemo_medication import ChemoMedPlan
# from cancer_subject.models.haart_medication import HaartMedRecord
#
# from ..forms import (
#     ActivityAndFunctioningForm, CancerDiagnosisForm, HaartRecordForm,
#     OncologyTreatmentPlanForm, TreatmentResponseForm, SymptomsAndTestingForm,
#     OncologyTreatmentCompletedForm, CurrentSymptomsForm)
# from ..models import (
#     HaartRecord, OncologyTreatmentPlan, TreatmentResponse,
#     OncologyTreatmentCompleted, ActivityAndFunctioning,
#     SymptomsAndTesting, CurrentSymptoms, CancerDiagnosis)
#
#
#
# class ChemoMedPlanInlineAdmin(TabularInlineMixin, admin.TabularInline):
#     model = ChemoMedPlan
#     form = ChemoMedPlanForm
#     extra = 1
#
#
#
#
# @admin.register(OncologyTreatmentCompleted, site=cancer_subject_admin)
# class OncologyTreatmentCompletedAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = OncologyTreatmentCompletedForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 "subject_visit",
#                 "patient_had_chemo",
#                 "patient_had_radiation",
#                 "patient_had_surgery",
#                 "treatment_detail",
#                 "patient_follow_up",
#                 "patient_follow_up_other",)}),)
#
#     radio_fields = {
#         "patient_had_chemo": admin.VERTICAL,
#         "patient_had_radiation": admin.VERTICAL,
#         "patient_had_surgery": admin.VERTICAL,
#         "patient_follow_up": admin.VERTICAL}
#
#
# @admin.register(CurrentSymptoms, site=cancer_subject_admin)
# class CurrentSymptomsAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = CurrentSymptomsForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 "subject_visit",
#                 "any_worry",
#                 "symptom_desc",
#                 "patient_own_remedy",
#                 "severity",
#                 "ra_advice",
#                 "outcome_update",)}),)
#
#     radio_fields = {
#         "any_worry": admin.VERTICAL, }
