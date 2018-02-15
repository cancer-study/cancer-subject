from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import cancer_subject_admin
from ..forms import BHHWhoIllnessForm
from ..models import BHHWhoIllness
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BHHWhoIllness, site=cancer_subject_admin)
class BHHWhoIllnessAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BHHWhoIllnessForm

    filter_horizontal = ("who_illness",)

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'who_illness_date',
                'who_illness',
                'who_illness_other')}),
        audit_fieldset_tuple
    )
