from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultHaematologyForm
from ..models import LabResultHaematology
from ..admin import LabResultAdminMixin


@admin.register(LabResultHaematology, site=cancer_subject_admin)
class LabResultHaematologyAdmin(LabResultAdminMixin):

    form = LabResultHaematologyForm
    fields = (
        "subject_visit",
        "haem_drawn_date",
        "hgb",
        "mcv",
        "wbc_count",
        "anc_count",
        "platelet",
        "comments")
    radio_fields = {}
