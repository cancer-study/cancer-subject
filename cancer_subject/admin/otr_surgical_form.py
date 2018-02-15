from django.contrib import admin

from edc_model_admin import TabularInlineMixin

from ..admin_site import cancer_subject_admin
from ..forms import OTRSurgicalForm
from ..models import OTRSurgical
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(OTRSurgical, site=cancer_subject_admin)
class OTRSurgicalAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OTRSurgicalForm
    fields = (
        "subject_visit",
        "operation_performed",
        "date_operation")
