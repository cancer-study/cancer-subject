from django.contrib import admin

from cancer_subject.admin.modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import LabResultChemistryForm
from ..models import LabResultChemistry


@admin.register(LabResultChemistry, site=cancer_subject_admin)
class LabResultChemistryAdmin(CrfModelAdminMixin):

    form = LabResultChemistryForm
    fields = (
        "subject_visit",
        "chem_drawn_date",
        "alanine",
        "aspartate",
        "bilirubin",
        "creatinine",
        "lactate",
        "comments")
    radio_fields = {}
