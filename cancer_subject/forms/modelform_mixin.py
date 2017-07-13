from django import forms

from edc_base.modelform_mixins import JSONModelFormMixin, CommonCleanModelFormMixin

from ..models import SubjectVisit


class SubjectModelFormMixin(CommonCleanModelFormMixin, JSONModelFormMixin, forms.ModelForm):

    visit_model = SubjectVisit
