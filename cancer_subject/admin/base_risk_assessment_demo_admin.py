from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentDemoForm
from ..models import BaseRiskAssessmentDemo
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentDemo, site=cancer_subject_admin)
class BaseRiskAssessmentDemoAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentDemoForm

    fields = (
        #"subject_visit",
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
