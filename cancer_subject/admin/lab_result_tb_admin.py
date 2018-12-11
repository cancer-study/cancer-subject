from django.contrib import admin

from cancer_subject.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultTbForm
from ..models import LabResultTb


@admin.register(LabResultTb, site=cancer_subject_admin)
class LabResultTbAdmin(CrfModelAdminMixin):

    form = LabResultTbForm
    fields = (
        "subject_visit",
        "tb_description",
        "tb_treatment",
        "tb_treatment_start")
    radio_fields = {
        "tb_treatment": admin.VERTICAL}
