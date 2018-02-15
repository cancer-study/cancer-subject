from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultHivForm
from ..models import LabResultHiv
from ..admin import LabResultAdminMixin


@admin.register(LabResultHiv, site=cancer_subject_admin)
class LabResultHivAdmin(LabResultAdminMixin):

    form = LabResultHivForm
    fields = (
        "subject_visit",
        "test_date",
        "test_result")
    radio_fields = {
        "test_result": admin.VERTICAL}
