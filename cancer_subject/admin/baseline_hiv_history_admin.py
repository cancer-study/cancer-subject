from django.contrib import admin

from edc_visit_tracking.modeladmin_mixins import VisitModelAdminMixin

from ..admin.modeladmin_mixins import CrfModelAdminMixin
from ..admin_site import cancer_subject_admin
from ..forms import (
    BaselineHIVHistoryForm, BHHHivTestForm, BHHWhoIllnessForm, BHHCd4Form)
from ..models import BaselineHIVHistory, BHHHivTest, BHHWhoIllness, BHHCd4
from .modeladmin_mixins import ModelAdminMixin


@admin.register(BaselineHIVHistory, site=cancer_subject_admin)
class BaselineHIVHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaselineHIVHistoryForm
    fields = (
        "subject_visit",
        "has_hiv_result",
        "had_who_illnesses",
        "has_cd4",
        "cd4_result",
        "cd4_drawn_date",
        "has_prior_cd4",
        "nadir_cd4",
        "nadir_cd4_drawn_date",
        "has_vl",
        "vl_result",
        "vl_drawn_date",)
    radio_fields = {
        "has_hiv_result": admin.VERTICAL,
        "had_who_illnesses": admin.VERTICAL,
        "has_cd4": admin.VERTICAL,
        "has_prior_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL}


@admin.register(BHHHivTest, site=cancer_subject_admin)
class BHHHivTestAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = BHHHivTestForm
    fields = (
        "subject_visit",
        "hiv_drawn_date",
        "hiv_testdate_est",
        "hiv_result",)
    radio_fields = {
        "hiv_testdate_est": admin.VERTICAL,
        "hiv_result": admin.VERTICAL}


@admin.register(BHHWhoIllness, site=cancer_subject_admin)
class BHHWhoIllnessAdmin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = BHHWhoIllnessForm
    fields = (
        "subject_visit",
        "who_illness_date",
        "who_illness",
        "who_illness_other",)
    filter_horizontal = (
        "who_illness",)


@admin.register(BHHCd4, site=cancer_subject_admin)
class BHHCd4Admin(VisitModelAdminMixin, ModelAdminMixin, admin.ModelAdmin):

    form = BHHCd4Form
    fields = (
        "subject_visit",
        "nadir_cd4",
        "nadir_cd4_drawn_date")
