from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin

from ambition_screening.models import SubjectScreening
from edc_base.modeladmin_mixins import (
    ModelAdminInstitutionMixin, audit_fieldset_tuple, audit_fields,
    ModelAdminNextUrlRedirectMixin)
from edc_consent.modeladmin_mixins import ModelAdminConsentMixin


from ..forms import SubjectConsentForm
from ..models import SubjectConsent
from ..admin_site import cancer_subject_admin


@admin.register(SubjectConsent, site=cancer_subject_admin)
class SubjectConsentAdmin(ModelAdminConsentMixin, ModelAdminRevisionMixin,
                          ModelAdminInstitutionMixin, ModelAdminNextUrlRedirectMixin,
                          admin.ModelAdmin):

    form = SubjectConsentForm

    fieldsets = (
        (None, {
            'fields': (
                'subject_screening',
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
                'id_type',
                'confirm_identity',
                'is_incarcerated',
                'may_store_samples',
                'store_genetic_samples',
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
    }

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "subject_screening":
            kwargs["queryset"] = SubjectScreening.objects.filter(
                id__exact=request.GET.get('subject_screening'))
        return super().formfield_for_foreignkey(
            db_field, request, **kwargs)

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)

    def view_on_site(self, obj):
        try:
            return reverse(
                'cancer_subject:dashboard_url', kwargs=dict(
                    subject_identifier=obj.subject_identifier))
        except NoReverseMatch:
            return super().view_on_site(obj)
