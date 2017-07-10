from django.contrib import admin

from edc.subject.consent.admin import BaseConsentModelAdmin

from ..models import SubjectConsent
from ..forms import SubjectConsentForm


# SubjectConsent
class SubjectConsentAdmin(BaseConsentModelAdmin):
    date_heirarchy = 'consent_datetime'
    form = SubjectConsentForm

    def __init__(self, *args, **kwargs):
        super(SubjectConsentAdmin, self).__init__(*args, **kwargs)
        self.fields = (
            "subject_identifier",
            #"original_identifier",
            "first_name",
            "last_name",
            "initials",
            "consent_datetime",
            "gender",
            "study_site",
            "is_literate",
            "witness_name",
            #"guardian_name",
            "dob",
            "is_dob_estimated",
            "identity",
            "identity_type",
            "confirm_identity",
#             "may_store_samples",
            "is_incarcerated",
            "comment",
            "consent_reviewed",
            "study_questions",
            "assessment_score",
            "consent_copy")
        self.radio_fields = {
            "study_site": admin.VERTICAL,
            "is_literate": admin.VERTICAL,
            "identity_type": admin.VERTICAL,
#             "may_store_samples": admin.VERTICAL,
            "gender": admin.VERTICAL,
            "is_dob_estimated": admin.VERTICAL,
            "is_incarcerated": admin.VERTICAL,
            "consent_reviewed": admin.VERTICAL,
            "study_questions": admin.VERTICAL,
            "assessment_score": admin.VERTICAL,
            "consent_copy": admin.VERTICAL}
        self.readonly_fields = ('subject_identifier',)
        self.list_filter = [
            'gender',
            'study_site',
            'is_verified',
            'is_verified_datetime',
            'may_store_samples',
            'consent_datetime',
            'created',
            'modified',
            'user_created',
            'user_modified',
            'hostname_created']
admin.site.register(SubjectConsent, SubjectConsentAdmin)
