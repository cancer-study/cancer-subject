from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentEatingForm
from ..models import BaseRiskAssessmentEating
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentEating, site=cancer_subject_admin)
class BaseRiskAssessmentEatingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentEatingForm
    fields = (
        #"subject_visit",
        "five_fruit",
        "meals_weekly",
        "meal_sorghum",
        "meal_millet",
        "meal_rice",
        "meal_peanuts")
    radio_fields = {
        "five_fruit": admin.VERTICAL}
