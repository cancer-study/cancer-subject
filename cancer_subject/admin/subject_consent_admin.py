from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.modeladmin_mixins import (
    ModelAdminInstitutionMixin, audit_fieldset_tuple, audit_fields,
    ModelAdminNextUrlRedirectMixin)

from edc_consent.modeladmin_mixins import ModelAdminConsentMixin

from ..admin_site import cancer_subject_admin
from ..forms import SubjectConsentForm
from ..models import SubjectConsent


@admin.register(SubjectConsent, site=cancer_subject_admin)
class SubjectConsentAdmin(ModelAdminConsentMixin, ModelAdminRevisionMixin,
                          ModelAdminInstitutionMixin,
                          ModelAdminNextUrlRedirectMixin, admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_identifier',
                'first_name',
                'last_name',
                'initials',
                'language',
                'is_literate',
                'witness_name',
                'consent_datetime',
                'dob',
                'guardian_name',
                'is_dob_estimated',
                'identity',
                'identity_type',
                'confirm_identity',
                'study_site',
                'is_incarcerated',
                'may_store_samples',
                'comment',
                'consent_reviewed',
                'study_questions',
                'assessment_score',
                'consent_copy')}),
        audit_fieldset_tuple)

    search_fields = ('subject_identifier',)

    radio_fields = {
        "assessment_score": admin.VERTICAL,
        "consent_copy": admin.VERTICAL,
        "consent_reviewed": admin.VERTICAL,
        "gender": admin.VERTICAL,
        "is_dob_estimated": admin.VERTICAL,
        "is_incarcerated": admin.VERTICAL,
        "is_literate": admin.VERTICAL,
        "language": admin.VERTICAL,
        "may_store_samples": admin.VERTICAL,
        "study_questions": admin.VERTICAL,
        "identity_type": admin.VERTICAL,
    }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)

    def view_on_site(self, obj):
        try:
            return reverse(
                'cancer_dashboard:consent_listboard_url', kwargs=dict(
                    subject_identifier=obj.subject_identifier))
        except NoReverseMatch:
            return super().view_on_site(obj)
