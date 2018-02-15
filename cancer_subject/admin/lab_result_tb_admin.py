from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultTbForm
from ..models import LabResultTb
from ..admin import LabResultAdminMixin


@admin.register(LabResultTb, site=cancer_subject_admin)
class LabResultTbAdmin(LabResultAdminMixin):

    form = LabResultTbForm
    fields = (
        "subject_visit",
        "tb_description",
        "tb_treatment",
        "tb_treatment_start")
    radio_fields = {
        "tb_treatment": admin.VERTICAL}
