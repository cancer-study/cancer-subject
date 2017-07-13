from django.contrib import admin

from ..models import (
    LabResult, LabResultHiv, LabResultCd4, LabResultViralload,
    LabResultHaematology, LabResultChemistry, LabResultTb)

from ..forms import (
    LabResultForm, LabResultHeightWeightForm, LabResultHivForm, LabResultCd4Form,
    LabResultChemistryForm, LabResultTbForm, LabResultHaematologyForm,
    LabResultViralloadForm)
from ..admin_site import cancer_subject_admin
from .modeladmin_mixins import ModelAdminMixin
from ..models import LabResultHeightWeight


@admin.register(LabResult, site=cancer_subject_admin)
class LabResultAdmin(ModelAdminMixin):

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


@admin.register(LabResultHeightWeight, site=cancer_subject_admin)
class LabResultHeightWeightAdmin(ModelAdminMixin):

    form = LabResultHeightWeightForm
    fields = (
        "subject_visit",
        "weight",
        "height",
        "cough2weeks",)
    radio_fields = {
        "cough2weeks": admin.VERTICAL}
    filter_horizontal = ()


@admin.register(LabResultHiv, site=cancer_subject_admin)
class LabResultHivAdmin(ModelAdminMixin):

    form = LabResultHivForm
    fields = (
        "subject_visit",
        "test_date",
        "test_result")
    radio_fields = {
        "test_result": admin.VERTICAL}


@admin.register(LabResultCd4, site=cancer_subject_admin)
class LabResultCd4Admin(ModelAdminMixin):

    form = LabResultCd4Form
    fields = (
        "subject_visit",
        "cd4_drawn_date",
        "cd4_result")
    radio_fields = {}


@admin.register(LabResultViralload, site=cancer_subject_admin)
class LabResultViralloadAdmin(ModelAdminMixin):

    form = LabResultViralloadForm
    fields = (
        "subject_visit",
        "report_datetime",
        "vl_drawn_date",
        "vl_result")
    radio_fields = {}


@admin.register(LabResultHaematology, site=cancer_subject_admin)
class LabResultHaematologyAdmin(ModelAdminMixin):

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


@admin.register(LabResultChemistry, site=cancer_subject_admin)
class LabResultChemistryAdmin(ModelAdminMixin):

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


@admin.register(LabResultTb, site=cancer_subject_admin)
class LabResultTbAdmin(ModelAdminMixin):

    form = LabResultTbForm
    fields = (
        "subject_visit",
        "tb_description",
        "tb_treatment",
        "tb_treatment_start")
    radio_fields = {
        "tb_treatment": admin.VERTICAL}
