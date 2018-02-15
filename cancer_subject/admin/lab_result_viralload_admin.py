from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultViralloadForm
from ..models import LabResultViralload
from ..admin import LabResultAdminMixin


@admin.register(LabResultViralload, site=cancer_subject_admin)
class LabResultViralloadAdmin(LabResultAdminMixin):

    form = LabResultViralloadForm
    fields = (
        "subject_visit",
        "report_datetime",
        "vl_drawn_date",
        "vl_result")
    radio_fields = {}
