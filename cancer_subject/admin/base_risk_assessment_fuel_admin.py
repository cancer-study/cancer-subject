from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentFuelForm
from ..models import BaseRiskAssessmentFuel
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentFuel, site=cancer_subject_admin)
class BaseRiskAssessmentFuelAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentFuelForm
    fields = (
        "subject_visit",
        "fuel_20y",
        "fuel_20y_other",
        "cooking",
        "fuel_mm",
        "fuel_mm_other",
        "cooking_mm")

    radio_fields = {
        "fuel_20y": admin.VERTICAL,
        "cooking": admin.VERTICAL,
        "fuel_mm": admin.VERTICAL,
        "cooking_mm": admin.VERTICAL}
