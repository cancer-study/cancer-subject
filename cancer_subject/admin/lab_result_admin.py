from django.contrib import admin
from .subject_visit_model_admin import SubjectVisitModelAdmin
from ..models import (LabResult, LabResultHeightWeight, LabResultHiv, LabResultCd4, LabResultViralload,
                                   LabResultHaematology, LabResultChemistry, LabResultTb)
from ..forms import (LabResultForm, LabResultHeightWeightForm, LabResultHivForm, LabResultCd4Form,
                                  LabResultViralloadForm, LabResultHaematologyForm, LabResultChemistryForm, LabResultTbForm)


# LabResult
class LabResultAdmin(SubjectVisitModelAdmin):

    form = LabResultForm
    fields = (
        "subject_visit",
        "has_hiv_result",
        "has_cd4",
        "has_vl",
        "has_haem",
        "has_chem",
        "has_other_abnormal",
        "other_abnormal",
        "tb_tests",
        "tb_prompt_other")
    radio_fields = {
        "has_hiv_result": admin.VERTICAL,
        "has_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL,
        "has_haem": admin.VERTICAL,
        "has_chem": admin.VERTICAL,
        "has_other_abnormal": admin.VERTICAL,
        "tb_tests": admin.VERTICAL}
    filter_horizontal = ()
admin.site.register(LabResult, LabResultAdmin)


# LabResultHeightWeight
class LabResultHeightWeightAdmin(SubjectVisitModelAdmin):

    form = LabResultHeightWeightForm
    fields = (
        "subject_visit",
        "weight",
        "height",
        "cough2weeks",)
    radio_fields = {
        "cough2weeks": admin.VERTICAL}
    filter_horizontal = ()
admin.site.register(LabResultHeightWeight, LabResultHeightWeightAdmin)


# LabResultHiv
class LabResultHivAdmin(SubjectVisitModelAdmin):

    form = LabResultHivForm
    fields = (
        "subject_visit",
        "test_date",
        "test_result")
    radio_fields = {
        "test_result": admin.VERTICAL}
admin.site.register(LabResultHiv, LabResultHivAdmin)


# LabResultCd4
class LabResultCd4Admin(SubjectVisitModelAdmin):

    form = LabResultCd4Form
    fields = (
        "subject_visit",
        "cd4_drawn_date",
        "cd4_result")
    radio_fields = {}
admin.site.register(LabResultCd4, LabResultCd4Admin)


# LabResultViralload
class LabResultViralloadAdmin(SubjectVisitModelAdmin):

    form = LabResultViralloadForm
    fields = (
        "subject_visit",
        "report_datetime",
        "vl_drawn_date",
        "vl_result")
    radio_fields = {}
admin.site.register(LabResultViralload, LabResultViralloadAdmin)


# LabResultHaematology
class LabResultHaematologyAdmin(SubjectVisitModelAdmin):

    form = LabResultHaematologyForm
    fields = (
        "subject_visit",
        "haem_drawn_date",
        "hgb",
        "mcv",
        "wbc_count",
        "anc_count",
        "platelet",
        "comments")
    radio_fields = {}
admin.site.register(LabResultHaematology, LabResultHaematologyAdmin)


# LabResultChemistry
class LabResultChemistryAdmin(SubjectVisitModelAdmin):

    form = LabResultChemistryForm
    fields = (
        "subject_visit",
        "chem_drawn_date",
        "alanine",
        "aspartate",
        "bilirubin",
        "creatinine",
        "lactate",
        "comments")
    radio_fields = {}
admin.site.register(LabResultChemistry, LabResultChemistryAdmin)


# LabResultTb
class LabResultTbAdmin(SubjectVisitModelAdmin):

    form = LabResultTbForm
    fields = (
        "subject_visit",
        "tb_description",
        "tb_treatment",
        "tb_treatment_start")
    radio_fields = {
        "tb_treatment": admin.VERTICAL}
admin.site.register(LabResultTb, LabResultTbAdmin)
