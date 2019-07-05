from django.contrib import admin

from edc_model_admin import TabularInlineMixin

from ..admin_site import cancer_subject_admin
from ..forms import OTRChemoForm
from ..forms.main import ChemoMedRecordForm
from ..models import ChemoMedRecord
from ..models import OTRChemo
from .modeladmin_mixins import CrfModelAdminMixin


class ChemoMedRecordInlineAdmin(TabularInlineMixin, admin.TabularInline):
    model = ChemoMedRecord
    form = ChemoMedRecordForm
    extra = 1


@admin.register(OTRChemo, site=cancer_subject_admin)
class OTRChemoAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OTRChemoForm
    inlines = [ChemoMedRecordInlineAdmin, ]
    fields = (
        "subject_visit",
        "chemo_intent",
        "chemo_delays",
        "why_delayed",
        "why_delayed_other",
        "chemo_reduced",
        "why_reduced",
        "why_reduced_other")
    radio_fields = {
        "chemo_intent": admin.VERTICAL,
        "chemo_delays": admin.VERTICAL,
        "why_delayed": admin.VERTICAL,
        "chemo_reduced": admin.VERTICAL,
        "why_reduced": admin.VERTICAL}
