from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentMiningForm
from ..models import BaseRiskAssessmentMining
from .modeladmin_mixins import CrfModelAdminMixin


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
