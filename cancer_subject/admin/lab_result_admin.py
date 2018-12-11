from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultForm
from ..models import LabResult
from .modeladmin_mixins import ModelAdminMixin


@admin.register(LabResult, site=cancer_subject_admin)
class LabResultAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = LabResultForm
    fields = (
        "subject_visit",
        "has_hiv_result",
        "has_cd4",
        "has_vl",
        "has_haem",
        "has_chem",
        "has_other_abnormal",
        "other_abnormal",
        "tb_tests",
        "tb_prompt_other")

    radio_fields = {
        "has_hiv_result": admin.VERTICAL,
        "has_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL,
        "has_haem": admin.VERTICAL,
        "has_chem": admin.VERTICAL,
        "has_other_abnormal": admin.VERTICAL,
        "tb_tests": admin.VERTICAL}
    filter_horizontal = ()
