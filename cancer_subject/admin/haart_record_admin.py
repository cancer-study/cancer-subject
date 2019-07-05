from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple, TabularInlineMixin

from .modeladmin_mixins import CrfModelAdminMixin

from ..admin_site import cancer_subject_admin
from ..forms import HaartRecordForm, HaartMedRecordForm
from ..models import HaartRecord, HaartMedRecord


class HaartMedRecordInlineAdmin(TabularInlineMixin, admin.TabularInline):

    model = HaartMedRecord
    form = HaartMedRecordForm
    extra = 1


@admin.register(HaartRecord, site=cancer_subject_admin)
class HaartRecordAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = HaartRecordForm
    inlines = [HaartMedRecordInlineAdmin, ]
    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                "subject_visit",
                "haart_status",
                "comments")}),
        audit_fieldset_tuple)

    radio_fields = {
        "haart_status": admin.VERTICAL}
