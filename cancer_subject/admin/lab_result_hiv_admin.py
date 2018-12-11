from django.contrib import admin

from cancer_subject.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultHivForm
from ..models import LabResultHiv


@admin.register(LabResultHiv, site=cancer_subject_admin)
class LabResultHivAdmin(CrfModelAdminMixin):

    form = LabResultHivForm
    fields = (
        "subject_visit",
        "test_date",
        "test_result")
    radio_fields = {
        "test_result": admin.VERTICAL}
