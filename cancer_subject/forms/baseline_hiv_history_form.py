from cancer_subject_validations.form_validators import BaseLineHivHistoryFormValidator

from ..models import BaselineHIVHistory
from .form_mixins import SubjectModelFormMixin


# BaselineHIVHistory
class BaselineHIVHistoryForm (SubjectModelFormMixin):

    form_validator_cls = BaseLineHivHistoryFormValidator

    class Meta:
        model = BaselineHIVHistory
        fields = '__all__'
