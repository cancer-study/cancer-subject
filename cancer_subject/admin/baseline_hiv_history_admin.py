from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import cancer_subject_admin
from ..forms import BaselineHIVHistoryForm
from ..models import BaselineHIVHistory
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaselineHIVHistory, site=cancer_subject_admin)
class BaselineHIVHistoryAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaselineHIVHistoryForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'has_hiv_result',
                'had_who_illnesses',
                'has_cd4',
                "cd4_result",
                "cd4_drawn_date",
                "has_prior_cd4",
                "nadir_cd4",
                "nadir_cd4_drawn_date",
                "has_vl",
                "vl_result",
                "vl_drawn_date",)}),
        audit_fieldset_tuple
    )
    radio_fields = {
        "has_hiv_result": admin.VERTICAL,
        "had_who_illnesses": admin.VERTICAL,
        "has_cd4": admin.VERTICAL,
        "has_prior_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL}
