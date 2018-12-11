from django.contrib import admin

from cancer_subject.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultHaematologyForm
from ..models import LabResultHaematology


@admin.register(LabResultHaematology, site=cancer_subject_admin)
class LabResultHaematologyAdmin(CrfModelAdminMixin):

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
