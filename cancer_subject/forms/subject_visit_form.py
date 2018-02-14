#  from django import forms
#
# from edc_consent.modelform_mixins import RequiresConsentModelFormMixin
# from edc_visit_tracking.form_validators import VisitFormValidator
#
# from ..models import SubjectVisit
#
#
# class SubjectVisitForm (RequiresConsentModelFormMixin, forms.ModelForm):
#
#     form_validator_cls = VisitFormValidator
#
#     class Meta:
#         model = SubjectVisit
#         fields = '__all__'
