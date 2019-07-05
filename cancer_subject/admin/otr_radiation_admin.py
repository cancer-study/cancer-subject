from django.contrib import admin

from ..admin_site import cancer_subject_admin
from ..forms import OTRRadiationForm
from ..models import OTRRadiation
from .modeladmin_mixins import CrfModelAdminMixin


@admin.register(OTRRadiation, site=cancer_subject_admin)
class OTRRadiationAdmin(CrfModelAdminMixin, admin.ModelAdmin):

    form = OTRRadiationForm
    fields = (
        "subject_visit",
        "radiation_details",
    )
    radio_fields = {
        "radiation_details": admin.VERTICAL,
    }
    instructions = [(
        "Review the recorded cancer type and stage information recorded and"
        " consider updating 'Cancer Diagnosis' form accordingly.")]
