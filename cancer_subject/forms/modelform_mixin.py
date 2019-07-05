from django import forms
from edc_base.sites.forms import SiteModelFormMixin
from edc_form_validators.form_validator_mixin import FormValidatorMixin
from edc_visit_tracking.modelform_mixins.visit_tracking_modelform_mixin import VisitTrackingModelFormMixin

from ..models import SubjectVisit


class SubjectModelFormMixin(SiteModelFormMixin, VisitTrackingModelFormMixin,
                            FormValidatorMixin, forms.ModelForm):

    visit_model = SubjectVisit
