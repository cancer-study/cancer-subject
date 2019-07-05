from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentSunForm
from ..models import BaseRiskAssessmentSun
from .modeladmin_mixins import CrfModelAdminMixin


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
