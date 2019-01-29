from django import forms
from edc_base.sites import SiteModelFormMixin
from edc_form_validators import FormValidatorMixin
from edc_form_validators.base_form_validator import INVALID_ERROR
from edc_visit_tracking.constants import UNSCHEDULED
from edc_visit_tracking.form_validators import VisitFormValidator as BaseVisitFormValidator

from ..models import SubjectVisit


class VisitFormValidator(BaseVisitFormValidator):

    def validate_visit_code_sequence_and_reason(self):
        appointment = self.cleaned_data.get('appointment')
        reason = self.cleaned_data.get('reason')
        if appointment:
            if (appointment.visit_code not in ['1000']
                    and reason == UNSCHEDULED):
                raise forms.ValidationError({
                    'reason': 'Invalid. This is not an unscheduled visit'},
                    code=INVALID_ERROR)


class SubjectVisitForm (
        SiteModelFormMixin, FormValidatorMixin, forms.ModelForm):

    form_validator_cls = VisitFormValidator

    class Meta:
        model = SubjectVisit
        fields = '__all__'
