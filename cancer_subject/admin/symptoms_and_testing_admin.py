from django.contrib import admin
from .modeladmin_mixins import CrfModelAdminMixin

from ..models import SymptomsAndTesting
from ..forms import SymptomsAndTestingForm
from ..admin_site import cancer_subject_admin


@admin.register(SymptomsAndTesting, site=cancer_subject_admin)
class SymptomsAndTestingAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = SymptomsAndTestingForm

    fieldsets = (
        (None, {
            'fields': (
                "report_datetime",
                "subject_visit",
                "symptom_prompt",
                "symptom_date",
                "medical_doctor_date",
                "trad_doctor_date",
                "facility_first_seen",
                "facility_first_seen_other",
                "hiv_tested",
                "hiv_test_result",
                "pos_date",
                "neg_date",
                "hiv_result",
                "arv_art_therapy",
                "arv_art_start_date",
                "arv_art_now",
                "art_art_stop_date",)}),)
    radio_fields = {
        "hiv_tested": admin.VERTICAL,
        "hiv_test_result": admin.VERTICAL,
        "hiv_result": admin.VERTICAL,
        "arv_art_therapy": admin.VERTICAL,
        "arv_art_now": admin.VERTICAL}
