from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultHeightWeightForm
from ..models import LabResultHeightWeight
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(LabResultHeightWeight, site=cancer_subject_admin)
class LabResultHeightWeightAdmin(CrfModelAdminMixin):

    form = LabResultHeightWeightForm
    fields = (
        "subject_visit",
        'report_datetime',
        "weight",
        "height",
        "cough2weeks",)
    radio_fields = {
        "cough2weeks": admin.VERTICAL}
    filter_horizontal = ()
