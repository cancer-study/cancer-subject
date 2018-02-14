from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentChemicalForm
from ..models import BaseRiskAssessmentChemical
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentChemical, site=cancer_subject_admin)
class BaseRiskAssessmentChemicalAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentChemicalForm
    fields = (
        #"subject_visit",
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
