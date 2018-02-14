from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentForm
from ..models import BaseRiskAssessment
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
