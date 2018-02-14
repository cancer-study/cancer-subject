from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentSmokingForm
from ..models import BaseRiskAssessmentSmoking
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentSmoking, site=cancer_subject_admin)
class BaseRiskAssessmentSmokingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentSmokingForm
    fields = (
        #"subject_visit",
        "smoke_now",
        "cigarette_smoking",
        "years_smoked",
        "cigarette_smoked",
        "when_quit",
        "years_smoked_before")
    radio_fields = {
        "smoke_now": admin.VERTICAL,
        "cigarette_smoking": admin.VERTICAL,
        "cigarette_smoked": admin.VERTICAL,
        "when_quit": admin.VERTICAL}
