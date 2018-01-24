from django import forms

# ,  CommonCleanModelFormMixin
from edc_base.modelform_mixins import JSONModelFormMixin

from ..models import SubjectVisit


class SubjectModelFormMixin(JSONModelFormMixin, forms.ModelForm):

    visit_model = SubjectVisit
