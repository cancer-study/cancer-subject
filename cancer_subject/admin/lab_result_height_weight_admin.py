from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultHeightWeightForm
from ..models import LabResultHeightWeight
from ..admin import LabResultAdminMixin


@admin.register(LabResultHeightWeight, site=cancer_subject_admin)
class LabResultHeightWeightAdmin(LabResultAdminMixin):

    form = LabResultHeightWeightForm
    fields = (
        "subject_visit",
        "weight",
        "height",
        "cough2weeks",)
    radio_fields = {
        "cough2weeks": admin.VERTICAL}
    filter_horizontal = ()
