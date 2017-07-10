from django.contrib import admin

from .registered_subject_model_admin import RegisteredSubjectModelAdmin
from ..forms import EnrollmentChecklistForm
from ..models import EnrollmentChecklist


class EnrollmentChecklistAdmin(RegisteredSubjectModelAdmin):

    form = EnrollmentChecklistForm
    fields = (
        "registered_subject",
        "registration_datetime",
        "has_diagnosis",
        "enrollment_site",)
    radio_fields = {
        "has_diagnosis": admin.VERTICAL,
        "enrollment_site": admin.VERTICAL, }
admin.site.register(EnrollmentChecklist, EnrollmentChecklistAdmin)
