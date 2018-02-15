from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import cancer_subject_admin
from ..forms import BHHCd4Form
from ..models import BHHCd4
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BHHCd4, site=cancer_subject_admin)
class BHHCd4Admin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BHHCd4Form

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'nadir_cd4',
                'nadir_cd4_drawn_date',)}),
        audit_fieldset_tuple
    )
