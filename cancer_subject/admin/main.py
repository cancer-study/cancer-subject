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
# class HaartMedRecordInlineAdmin(TabularInlineMixin, admin.TabularInline):
#
#     model = HaartMedRecord
#     form = HaartMedRecordForm
#     extra = 1
#
#
# class ChemoMedPlanInlineAdmin(TabularInlineMixin, admin.TabularInline):
#     model = ChemoMedPlan
#     form = ChemoMedPlanForm
#     extra = 1
#
#
# @admin.register(ActivityAndFunctioning, site=cancer_subject_admin)
# class ActivityAndFunctioningAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = ActivityAndFunctioningForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'report_datetime',
#                 'subject_visit',
#                 "health_rate",
#                 "health_problems",
#                 "difficulty_work",
#                 "bodily_pain",
#                 "energy",
#                 "health_probs_limit",
#                 "emotional_probs",
#                 "probs_from_work",
#                 "perform_status")}),
#         audit_fieldset_tuple
#     )
#     radio_fields = {
#         "health_rate": admin.VERTICAL,
#         "health_problems": admin.VERTICAL,
#         "difficulty_work": admin.VERTICAL,
#         "bodily_pain": admin.VERTICAL,
#         "energy": admin.VERTICAL,
#         "health_probs_limit": admin.VERTICAL,
#         "emotional_probs": admin.VERTICAL,
#         "probs_from_work": admin.VERTICAL,
#         "perform_status": admin.VERTICAL}
#
#
# @admin.register(CancerDiagnosis, site=cancer_subject_admin)
# class CancerDiagnosisAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = CancerDiagnosisForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'report_datetime',
#                 'subject_visit',
#                 "onco_number",
#                 "pathology_number",
#                 "pm_number",
#                 "diagnosis",
#                 "cancer_category",
#                 "symptom_prompt",
#                 "symptom_prompt_other",
#                 "symptom_first_noticed",
#                 "first_evaluation",
#                 "trad_evaluation",
#                 "date_diagnosed",
#                 "diagnosis_basis",
#                 "diagnosis_basis_other",
#                 "diagnosis_word",
#                 "cancer_site",
#                 "clinical_diagnosis",
#                 "tumour",
#                 "tumour_basis",
#                 "lymph_nodes",
#                 "lymph_basis",
#                 "metastasis",
#                 "metastasis_basis",
#                 "cancer_stage",
#                 "cancer_stage_modifier",
#                 "any_other_results",
#                 "paper_documents",
#                 "results_to_record",
#                 "results_to_record_other",)}),
#         audit_fieldset_tuple
#     )
#     radio_fields = {
#         "diagnosis": admin.VERTICAL,
#         "cancer_category": admin.VERTICAL,
#         "symptom_prompt": admin.VERTICAL,
#         "diagnosis_basis": admin.VERTICAL,
#         "tumour": admin.VERTICAL,
#         "tumour_basis": admin.VERTICAL,
#         "lymph_nodes": admin.VERTICAL,
#         "lymph_basis": admin.VERTICAL,
#         "metastasis": admin.VERTICAL,
#         "metastasis_basis": admin.VERTICAL,
#         "cancer_stage": admin.VERTICAL,
#         "cancer_stage_modifier": admin.VERTICAL,
#         "any_other_results": admin.VERTICAL}
#     filter_horizontal = ('results_to_record',)
#
#
# @admin.register(HaartRecord, site=cancer_subject_admin)
# class HaartRecordAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = HaartRecordForm
#     inlines = [HaartMedRecordInlineAdmin, ]
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'report_datetime',
#                 "subject_visit",
#                 "haart_status",
#                 "comments")}),
#         audit_fieldset_tuple)
#
#     radio_fields = {
#         "haart_status": admin.VERTICAL}
#
#
# @admin.register(OncologyTreatmentPlan, site=cancer_subject_admin)
# class OncologyTreatmentPlanAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = OncologyTreatmentPlanForm
#     inlines = [ChemoMedPlanInlineAdmin, ]
#     fieldsets = (
#         (None, {
#             'fields': (
#                 "subject_visit",
#                 "treatment_goal",
#                 "treatment_plan",
#                 "chemotherapy",
#                 "chemo_intent",
#                 "radiation_plan",
#                 "surgical_plan",
#                 "planned_operation",
#                 "comments")}),
#         audit_fieldset_tuple)
#
#     radio_fields = {
#         "treatment_goal": admin.VERTICAL,
#         "treatment_plan": admin.VERTICAL,
#         "chemotherapy": admin.VERTICAL,
#         "chemo_intent": admin.VERTICAL,
#         "radiation_plan": admin.VERTICAL,
#         "surgical_plan": admin.VERTICAL}
#
#
# @admin.register(TreatmentResponse, site=cancer_subject_admin)
# class TreatmentResponseAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = TreatmentResponseForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 "subject_visit",
#                 "tx_response_class",
#                 "tx_info_determinant",
#                 "tx_response_date",
#                 "tx_response")}),)
#     radio_fields = {
#         "tx_response_class": admin.VERTICAL}
#     filter_horizontal = (
#         "tx_info_determinant",)
#
#
# @admin.register(SymptomsAndTesting, site=cancer_subject_admin)
# class SymptomsAndTestingAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = SymptomsAndTestingForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 "report_datetime",
#                 "subject_visit",
#                 "symptom_prompt",
#                 "symptom_date",
#                 "medical_doctor_date",
#                 "trad_doctor_date",
#                 "facility_first_seen",
#                 "facility_first_seen_other",
#                 "hiv_tested",
#                 "hiv_test_result",
#                 "pos_date",
#                 "neg_date",
#                 "hiv_result",
#                 "arv_art_therapy",
#                 "arv_art_start_date",
#                 "arv_art_now",
#                 "art_art_stop_date",)}),)
#     radio_fields = {
#         "hiv_tested": admin.VERTICAL,
#         "hiv_test_result": admin.VERTICAL,
#         "hiv_result": admin.VERTICAL,
#         "arv_art_therapy": admin.VERTICAL,
#         "arv_art_now": admin.VERTICAL}
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
