from django.contrib import admin
from ..models import (
    BaseRiskAssessment, BaseRiskAssessmentAlcohol, BaseRiskAssessmentCancer,
    BaseRiskAssessmentChemical, BaseRiskAssessmentDemo, BaseRiskAssessmentEating,
    BaseRiskAssessmentMining, BaseRiskAssessmentSmoking, BaseRiskAssessmentSun)
from ..forms import (
    BaseRiskAssessmentForm, BaseRiskAssessmentAlcoholForm, BaseRiskAssessmentCancerForm,
    BaseRiskAssessmentChemicalForm, BaseRiskAssessmentDemoForm, BaseRiskAssessmentEatingForm,
    BaseRiskAssessmentMiningForm, BaseRiskAssessmentSmokingForm, BaseRiskAssessmentSunForm)

from ..admin_site import cancer_subject_admin
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessment, site=cancer_subject_admin)
class BaseRiskAssessmentAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentForm
    fields = (
        "subject_visit",
        # "participant_interviewed",
        "hepatitis",
        "tuberculosis",
        "year_tb",
        "has_worked_mine",
        "has_smoked",
        "age_firstsex",
        "has_alcohol",
        "tradmedicine",
        "is_albino")
    radio_fields = {
        # "participant_interviewed": admin.VERTICAL,
        "hepatitis": admin.VERTICAL,
        "tuberculosis": admin.VERTICAL,
        "has_worked_mine": admin.VERTICAL,
        "has_smoked": admin.VERTICAL,
        "age_firstsex": admin.VERTICAL,
        "has_alcohol": admin.VERTICAL,
        "tradmedicine": admin.VERTICAL,
        "is_albino": admin.VERTICAL}


# BaseRiskAssessmentAlcohol
@admin.register(BaseRiskAssessmentAlcohol, site=cancer_subject_admin)
class BaseRiskAssessmentAlcoholAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentAlcoholForm
    fields = (
        "subject_visit",
        "alcohol_weekly",
        "amount_drinking")
    radio_fields = {}


@admin.register(BaseRiskAssessmentCancer, site=cancer_subject_admin)
class BaseRiskAssessmentCancerAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentCancerForm
    fields = (
        "subject_visit",
        "family_cancer",
        "family_cancer_type",
        "family_cancer_other",
        "had_previous_cancer",
        "previous_cancer",
        "previous_cancer_other")
    radio_fields = {
        "family_cancer": admin.VERTICAL,
        "family_cancer_type": admin.VERTICAL,
        "had_previous_cancer": admin.VERTICAL,
        "previous_cancer": admin.VERTICAL}


@admin.register(BaseRiskAssessmentChemical, site=cancer_subject_admin)
class BaseRiskAssessmentChemicalAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentChemicalForm
    fields = (
        "subject_visit",
        "asbestos",
        "asbestos_no_protection",
        "chemicals",
        "chemicals_time",
        "arsenic_smelting",
        "total_time_no_protection")
    radio_fields = {
        "asbestos": admin.VERTICAL,
        "asbestos_no_protection": admin.VERTICAL,
        "chemicals": admin.VERTICAL,
        "chemicals_time": admin.VERTICAL,
        "arsenic_smelting": admin.VERTICAL,
        "total_time_no_protection": admin.VERTICAL}


@admin.register(BaseRiskAssessmentDemo, site=cancer_subject_admin)
class BaseRiskAssessmentDemoAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentDemoForm

    fields = (
        "subject_visit",
        "marital_status",
        "marital_status_other",
        "race",
        "race_other",
        "ethnic_grp",
        "ethnic_grp_other",
        "community",
        "community_other",
        "district20",
        "setting20",
        "district",
        "setting",
        "education",
        "occupation",
        "occupation_other",
        "money_provide",
        "money_provide_other",
        "money_earned",
        "electricity",
        "toilet",
        "toilet_other",
        "household_people",
        "food_security")
    radio_fields = {
        "marital_status": admin.VERTICAL,
        "race": admin.VERTICAL,
        "ethnic_grp": admin.VERTICAL,
        "district20": admin.VERTICAL,
        "setting20": admin.VERTICAL,
        "district": admin.VERTICAL,
        "setting": admin.VERTICAL,
        "education": admin.VERTICAL,
        "occupation": admin.VERTICAL,
        "money_provide": admin.VERTICAL,
        "money_earned": admin.VERTICAL,
        "electricity": admin.VERTICAL,
        "toilet": admin.VERTICAL,
        "food_security": admin.VERTICAL}


@admin.register(BaseRiskAssessmentEating, site=cancer_subject_admin)
class BaseRiskAssessmentEatingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentEatingForm
    fields = (
        "subject_visit",
        "five_fruit",
        "meals_weekly",
        "meal_sorghum",
        "meal_millet",
        "meal_rice",
        "meal_peanuts")
    radio_fields = {
        "five_fruit": admin.VERTICAL}


# @admin.register(BaseRiskAssessmentFemale, site=cancer_subject_admin)
# class BaseRiskAssessmentFemaleAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = BaseRiskAssessmentFemaleForm
#     fields = (
#         "subject_visit",
#         "age_period",
#         "children",
#         "years_breastfed")
#     radio_fields = {
#         "years_breastfed": admin.VERTICAL}


# @admin.register(BaseRiskAssessmentFemale, site=cancer_subject_admin)
# class BaseRiskAssessmentFuelAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = BaseRiskAssessmentFuelForm
#     fields = (
#         "subject_visit",
#         "fuel_20y",
#         "fuel_20y_other",
#         "cooking",
#         "fuel_mm",
#         "fuel_mm_other",
#         "cooking_mm")
# 
#     radio_fields = {
#         "fuel_20y": admin.VERTICAL,
#         "cooking": admin.VERTICAL,
#         "fuel_mm": admin.VERTICAL,
#         "cooking_mm": admin.VERTICAL}


@admin.register(BaseRiskAssessmentMining, site=cancer_subject_admin)
class BaseRiskAssessmentMiningAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentMiningForm
    fields = (
        "subject_visit",
        "mine_time",
        "mine_type",
        "mine_prompt_other",
        "mine_underground",
        "mine_underground_time",
        "last_mine")
    radio_fields = {
        "mine_time": admin.VERTICAL,
        "mine_type": admin.VERTICAL,
        "mine_underground": admin.VERTICAL,
        "mine_underground_time": admin.VERTICAL}


@admin.register(BaseRiskAssessmentSmoking, site=cancer_subject_admin)
class BaseRiskAssessmentSmokingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentSmokingForm
    fields = (
        "subject_visit",
        "smoke_now",
        "cigarette_smoking",
        "years_smoked",
        "cigarette_smoked",
        "when_quit",
        "years_smoked_before")
    radio_fields = {
        "smoke_now": admin.VERTICAL,
        "cigarette_smoking": admin.VERTICAL,
        "cigarette_smoked": admin.VERTICAL,
        "when_quit": admin.VERTICAL}


@admin.register(BaseRiskAssessmentSun, site=cancer_subject_admin)
class BaseRiskAssessmentSunAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentSunForm
    fields = (
        "subject_visit",
        "hours_outdoor",
        "sleeved_shirt",
        "hat",
        "shade_umbrella",
        "sunglasses")
    radio_fields = {
        "hours_outdoor": admin.VERTICAL,
        "sleeved_shirt": admin.VERTICAL,
        "hat": admin.VERTICAL,
        "shade_umbrella": admin.VERTICAL,
        "sunglasses": admin.VERTICAL}
