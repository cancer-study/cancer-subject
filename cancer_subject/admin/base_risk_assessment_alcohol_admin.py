from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import BaseRiskAssessmentAlcoholForm
from ..models import BaseRiskAssessmentAlcohol
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(BaseRiskAssessmentAlcohol, site=cancer_subject_admin)
class BaseRiskAssessmentAlcoholAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = BaseRiskAssessmentAlcoholForm
    fields = (
        "subject_visit",
        "alcohol_weekly",
        "amount_drinking")
    radio_fields = {}
