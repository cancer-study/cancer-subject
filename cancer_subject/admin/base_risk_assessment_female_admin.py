from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentFemaleForm
from ..models import BaseRiskAssessmentFemale
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentFemale, site=cancer_subject_admin)
class BaseRiskAssessmentFemaleAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentFemaleForm
    fields = (
        "subject_visit",
        "age_period",
        "children",
        "years_breastfed")
    radio_fields = {
        "years_breastfed": admin.VERTICAL}
