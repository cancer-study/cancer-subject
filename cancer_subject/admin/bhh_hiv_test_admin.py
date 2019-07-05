from django.contrib import admin

from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import cancer_subject_admin
from ..forms import BHHHivTestForm
from ..models import BHHHivTest
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BHHHivTest, site=cancer_subject_admin)
class BHHHivTestAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BHHHivTestForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_visit',
                'hiv_drawn_date',
                'hiv_testdate_est',
                'hiv_result')}),
        audit_fieldset_tuple
    )
    radio_fields = {
        "hiv_testdate_est": admin.VERTICAL,
        "hiv_result": admin.VERTICAL}
