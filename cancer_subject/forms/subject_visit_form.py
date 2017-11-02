from django import forms
from django.conf import settings

from edc_consent.modelform_mixins import RequiresConsentModelFormMixin
from edc_consent.site_consents import site_consents
from edc_visit_tracking.form_validators import VisitFormValidator

from ..models import SubjectVisit


class SubjectVisitForm (RequiresConsentModelFormMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
