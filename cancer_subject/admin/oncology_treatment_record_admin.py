from django.contrib import admin


from ..admin_site import cancer_subject_admin
from ..forms import OncologyTreatmentRecordForm
from ..models import OncologyTreatmentRecord
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(OncologyTreatmentRecord, site=cancer_subject_admin)
class OncologyTreatmentRecordAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OncologyTreatmentRecordForm
    fields = (
        "subject_visit",
        "chemo_received",
        "radiation_received",
        "surgical_therapy",
        "comments")
    radio_fields = {
        "chemo_received": admin.VERTICAL,
        "radiation_received": admin.VERTICAL,
        "surgical_therapy": admin.VERTICAL}
    instructions = [("Note to Interviewer: If any of the answers below"
                     " are yes, make arrangements to obtain records or"
                     " review records over the phone")]
