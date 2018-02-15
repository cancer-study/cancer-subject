from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentCancerForm
from ..models import BaseRiskAssessmentCancer
from .modeladmin_mixins import CrfModelAdminMixin


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
