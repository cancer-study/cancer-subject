from django.contrib import admin
from edc.subject.registration.models import RegisteredSubject
from edc.base.modeladmin.admin import BaseTabularInline, BaseModelAdmin
from .subject_off_study_model_admin import SubjectOffStudyModelAdmin
from .subject_visit_model_admin import SubjectVisitModelAdmin
from .registered_subject_model_admin import RegisteredSubjectModelAdmin
from ..models import (HaartMedRecord, ChemoMedPlan, Locator, SubjectDeath, SubjectVisit,
                     SubjectOffStudy, ActivityAndFunctioning, CancerDiagnosis, HaartRecord,
                     OncologyTreatmentPlan, TreatmentResponse, SymptomsAndTesting, EnrollmentSite,
                     OncologyTreatmentCompleted, CurrentSymptoms)
from ..forms import (LocatorForm, SubjectDeathForm, SubjectOffStudyForm,
                     ActivityAndFunctioningForm, CancerDiagnosisForm, HaartRecordForm,
                     OncologyTreatmentPlanForm, TreatmentResponseForm, SymptomsAndTestingForm,
                     OncologyTreatmentCompletedForm, CurrentSymptomsForm)


class LocatorAdmin(SubjectVisitModelAdmin):

    form = LocatorForm
    fields = (
        'subject_visit',
        'date_signed',
        'mail_address',
        'home_visit_permission',
        'physical_address',
        'may_follow_up',
        'subject_cell',
        'subject_cell_alt',
        'subject_phone',
        'subject_phone_alt',
        'may_contact_someone',
        'contact_name',
        'contact_rel',
        'contact_cell',
        'alt_contact_cell_number',
        'contact_phone',
        'has_alt_contact',
        'alt_contact_name',
        'alt_contact_rel',
        'alt_contact_cell',
        'other_alt_contact_cell',
        'alt_contact_tel',
        'may_call_work',
        'subject_work_place',
        'subject_work_phone',
        'home_village',
        'local_clinic',)
    radio_fields = {
        "home_visit_permission": admin.VERTICAL,
        "may_follow_up": admin.VERTICAL,
        "has_alt_contact": admin.VERTICAL,
        "may_call_work": admin.VERTICAL,
        "may_contact_someone": admin.VERTICAL, }
admin.site.register(Locator, LocatorAdmin)


class HaartMedRecordInlineAdmin(BaseTabularInline):
    model = HaartMedRecord


class ChemoMedPlanInlineAdmin(BaseTabularInline):
    exclude = ('dose_category',)
    model = ChemoMedPlan


# SubjectDeath
class SubjectDeathAdmin(RegisteredSubjectModelAdmin):

    form = SubjectDeathForm
    fields = (
        "registered_subject",
        "subject_visit",
        "death_date",
        "is_death_date_estimated",
        "death_cause_info",
        "death_cause_info_other",
        "death_cause",
        "death_cause_category",
        "death_cause_other",
        "comment")
    list_filter = [
            'created',
            'user_created',
            'hostname_created',
            'modified',
            'user_modified',
            'hostname_modified',
            'registered_subject__gender',
            'registered_subject__study_site',
            'registered_subject__registration_datetime',
            ]
#     list_display = ('registered_subject', 'subject_visit', 'death_date', 'created', 'user_created',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject_visit":
            #subject_visit = SubjectVisit.objects.filter(id=request.GET.get(db_field.name))
            kwargs["queryset"] = SubjectVisit.objects.filter(id=request.GET.get(db_field.name, None))
        return super(SubjectDeathAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(SubjectDeath, SubjectDeathAdmin)


# SubjectOffStudy
class SubjectOffStudyAdmin(SubjectOffStudyModelAdmin):
    form = SubjectOffStudyForm
    fields = (
        "registered_subject",
        "subject_visit",
        "offstudy_date",
        "reason",
        "reason_other",
        "has_scheduled_data",
        "comment")
    radio_fields = {
        "has_scheduled_data": admin.VERTICAL}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject_visit":
            kwargs["queryset"] = SubjectVisit.objects.filter(id__exact=request.GET.get('subject_visit', 0))
        return super(SubjectOffStudyAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(SubjectOffStudy, SubjectOffStudyAdmin)


# ActivityAndFunctioning
class ActivityAndFunctioningAdmin(SubjectVisitModelAdmin):

    form = ActivityAndFunctioningForm
    fields = (
        "report_datetime",
        "subject_visit",
        "health_rate",
        "health_problems",
        "difficulty_work",
        "bodily_pain",
        "energy",
        "health_probs_limit",
        "emotional_probs",
        "probs_from_work",
        "perform_status")
    radio_fields = {
        "health_rate": admin.VERTICAL,
        "health_problems": admin.VERTICAL,
        "difficulty_work": admin.VERTICAL,
        "bodily_pain": admin.VERTICAL,
        "energy": admin.VERTICAL,
        "health_probs_limit": admin.VERTICAL,
        "emotional_probs": admin.VERTICAL,
        "probs_from_work": admin.VERTICAL,
        "perform_status": admin.VERTICAL}
admin.site.register(ActivityAndFunctioning, ActivityAndFunctioningAdmin)


# CancerDiagnosis
class CancerDiagnosisAdmin(SubjectVisitModelAdmin):

    form = CancerDiagnosisForm
    fields = (
        "subject_visit",
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
#         "electronic_documents",
        "results_to_record",
        "results_to_record_other",)
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
admin.site.register(CancerDiagnosis, CancerDiagnosisAdmin)


# HaartRecord
class HaartRecordAdmin(SubjectVisitModelAdmin):

    form = HaartRecordForm
    inlines = [HaartMedRecordInlineAdmin, ]
    fields = (
        "subject_visit",
        "haart_status",
        "comments")
    radio_fields = {
        "haart_status": admin.VERTICAL}
admin.site.register(HaartRecord, HaartRecordAdmin)


# OncologyTreatmentPlan
class OncologyTreatmentPlanAdmin(SubjectVisitModelAdmin):

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
admin.site.register(OncologyTreatmentPlan, OncologyTreatmentPlanAdmin)


# TreatmentResponse
class TreatmentResponseAdmin(SubjectVisitModelAdmin):

    form = TreatmentResponseForm
    fields = (
        "subject_visit",
        "tx_response_class",
        "tx_info_determinant",
        "tx_response_date",
        "tx_response")
    radio_fields = {
        "tx_response_class": admin.VERTICAL}
    filter_horizontal = (
        "tx_info_determinant",)
admin.site.register(TreatmentResponse, TreatmentResponseAdmin)


# SymptomsAndTesting
class SymptomsAndTestingAdmin(SubjectVisitModelAdmin):

    form = SymptomsAndTestingForm
    fields = (
        "report_datetime",
        "subject_visit",
        "symptom_prompt",
        "symptom_date",
        "medical_doctor_date",
        "trad_doctor_date",
        "facility_first_seen",
        "facility_first_seen_other",
        "hiv_tested",
        "hiv_test_result",
        "pos_date",
        "neg_date",
        "hiv_result",
        "arv_art_therapy",
        "arv_art_start_date",
        "arv_art_now",
        "art_art_stop_date",)
    radio_fields = {
        "hiv_tested": admin.VERTICAL,
        "hiv_test_result": admin.VERTICAL,
        "hiv_result": admin.VERTICAL,
        "arv_art_therapy": admin.VERTICAL,
        "arv_art_now": admin.VERTICAL}
admin.site.register(SymptomsAndTesting, SymptomsAndTestingAdmin)


class EnrollmentSiteAdmin(BaseModelAdmin):
    list_display = ("site_name",)
admin.site.register(EnrollmentSite, EnrollmentSiteAdmin)


# OncologyTreatmentCompleted
class OncologyTreatmentCompletedAdmin(SubjectVisitModelAdmin):

    form = OncologyTreatmentCompletedForm
    fields = (
        "subject_visit",
        "patient_had_chemo",
        "patient_had_radiation",
        "patient_had_surgery",
        "treatment_detail",
        "patient_follow_up",
        "patient_follow_up_other",)
    radio_fields = {
        "patient_had_chemo": admin.VERTICAL,
        "patient_had_radiation": admin.VERTICAL,
        "patient_had_surgery": admin.VERTICAL,
        "patient_follow_up": admin.VERTICAL}
admin.site.register(OncologyTreatmentCompleted, OncologyTreatmentCompletedAdmin)


# CurrentSymptoms
class CurrentSymptomsAdmin(SubjectVisitModelAdmin):

    form = CurrentSymptomsForm
    fields = (
        "subject_visit",
        "any_worry",
        "symptom_desc",
        "patient_own_remedy",
        "severity",
#         "pain",
        "ra_advice",
        "outcome_update",
        )
    radio_fields = {
        "any_worry": admin.VERTICAL,
        }
admin.site.register(CurrentSymptoms, CurrentSymptomsAdmin)
