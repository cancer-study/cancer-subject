from django import forms

from .form_mixins import SubjectModelFormMixin
from ..models import (
    BaseRiskAssessment, BaseRiskAssessmentAlcohol,
    BaseRiskAssessmentCancer, BaseRiskAssessmentChemical,
    BaseRiskAssessmentDemo, BaseRiskAssessmentEating,
    BaseRiskAssessmentFemale, BaseRiskAssessmentFuel,
    BaseRiskAssessmentMining, BaseRiskAssessmentSmoking,
    BaseRiskAssessmentSun)
from edc_constants.constants import YES


class BaseRiskAssessmentForm (SubjectModelFormMixin):
    def clean(self):

        cleaned_data = self.cleaned_data
        # validating tubercolosis
        if cleaned_data.get('tuberculosis') == YES and not cleaned_data.get('year_tb'):
            raise forms.ValidationError('If patient has ever had tubercolosis, please provide the year TB was diagnosed')
        cleaned_data = super(BaseRiskAssessmentForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaseRiskAssessment


# BaseRiskAssessmentAlcohol
class BaseRiskAssessmentAlcoholForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentAlcohol


# BaseRiskAssessmentCancer
class BaseRiskAssessmentCancerForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('family_cancer') == YES and not cleaned_data.get('family_cancer_type'):
            raise forms.ValidationError('If any relative has had any cancer, what type was it')
        if cleaned_data.get('had_previous_cancer') == YES and not cleaned_data.get('previous_cancer'):
            raise forms.ValidationError('If subject has had a previous cancer, what kind of cancer was it')
        cleaned_data = super(BaseRiskAssessmentCancerForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaseRiskAssessmentCancer


# BaseRiskAssessmentChemical
class BaseRiskAssessmentChemicalForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('asbestos') == YES and not cleaned_data.get('asbestos_no_protection'):
            raise forms.ValidationError('If subject has worked with asbestos, how long has he/she worked with it')
        if cleaned_data.get('chemicals') == YES and not cleaned_data.get('chemicals_time'):
            raise forms.ValidationError('If subject has worked with any of the chemicals, how long has it been')
        if cleaned_data.get('arsenic_smelting') == YES and not cleaned_data.get('total_time_no_protection'):
            raise forms.ValidationError('If subject has ever been involved in arsenic smelting, how long has it been')
        cleaned_data = super(BaseRiskAssessmentChemicalForm, self).clean()
        return cleaned_data

    class Meta:
        model = BaseRiskAssessmentChemical


# BaseRiskAssessmentDemo
class BaseRiskAssessmentDemoForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentDemo


# BaseRiskAssessmentEating
class BaseRiskAssessmentEatingForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentEating


# BaseRiskAssessmentFemale
class BaseRiskAssessmentFemaleForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentFemale


# BaseRiskAssessmentFuel
class BaseRiskAssessmentFuelForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentFuel


# BaseRiskAssessmentMining
class BaseRiskAssessmentMiningForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentMining


# BaseRiskAssessmentSmoking
class BaseRiskAssessmentSmokingForm (SubjectModelFormMixin):
    def clean(self):
        cleaned_data = super(BaseRiskAssessmentSmokingForm, self).clean()

        if cleaned_data.get('smoke_now') == 'yes' and not cleaned_data.get('cigarette_smoking'):
            raise forms.ValidationError('If subject is smoking now, how many cigarettes per day does he/she smoke')
        if cleaned_data.get('smoke_now') == 'yes' and not cleaned_data.get('years_smoked'):
            raise forms.ValidationError('Subject smokes. How many years has he/she smoked?')

        if cleaned_data.get('smoke_now') == 'yes' and cleaned_data.get('cigarette_smoked'):
            raise forms.ValidationError('Subject smokes. DON\'T answer question about: How many cigarettes DID you smoke per day')
        if cleaned_data.get('smoke_now') == 'yes' and cleaned_data.get('when_quit'):
            raise forms.ValidationError('Subject smokes. You cannot give info about quitting.')
        if cleaned_data.get('smoke_now') == 'yes' and cleaned_data.get('years_smoked_before'):
            raise forms.ValidationError('Subject smokes. You CANNOT give details about quitting.')

        if cleaned_data.get('smoke_now') == 'no' and cleaned_data.get('cigarette_smoking'):
            raise forms.ValidationError('Subject quit smoking. DO NOT give any details about smoking NOW.')
        if cleaned_data.get('smoke_now') == 'no' and cleaned_data.get('years_smoked'):
            raise forms.ValidationError('Subject quit smoking. DO NOT give any details about smoking NOW.')

        if cleaned_data.get('smoke_now') == 'no' and not cleaned_data.get('cigarette_smoked'):
            raise forms.ValidationError('Subject used to smoke but quit. How many cigarettes did he/she smoke per day?')
        if cleaned_data.get('smoke_now') == 'no' and not cleaned_data.get('when_quit'):
            raise forms.ValidationError('Subject used to smoke but quit. When did he/she quit?')
        if cleaned_data.get('smoke_now') == 'no' and not cleaned_data.get('years_smoked_before'):
            raise forms.ValidationError('Subject used to smoke but quit. For how many years did he/she smoke before he/she quit?')

        return cleaned_data

    class Meta:
        model = BaseRiskAssessmentSmoking


# BaseRiskAssessmentSun
class BaseRiskAssessmentSunForm (SubjectModelFormMixin):

    class Meta:
        model = BaseRiskAssessmentSun
