from django.contrib import admin

from cancer_subject.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultViralloadForm
from ..models import LabResultViralload


@admin.register(LabResultViralload, site=cancer_subject_admin)
class LabResultViralloadAdmin(CrfModelAdminMixin):

    form = LabResultViralloadForm
    fields = (
        "subject_visit",
        "report_datetime",
        "vl_drawn_date",
        "vl_result")
    radio_fields = {}
