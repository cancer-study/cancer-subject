from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultCd4Form
from ..models import LabResultCd4
from ..admin import LabResultAdminMixin


@admin.register(LabResultCd4, site=cancer_subject_admin)
class LabResultCd4Admin(LabResultAdminMixin):

    form = LabResultCd4Form
    fields = (
        "subject_visit",
        "cd4_drawn_date",
        "cd4_result")
    radio_fields = {}
