from .modelform_mixin import SubjectModelFormMixin
from ..models import (ActivityAndFunctioning, ChemoMedRecord,
                      HaartRecord, HaartMedRecord)


class ActivityAndFunctioningForm (SubjectModelFormMixin):

    class Meta:
        model = ActivityAndFunctioning
        fields = '__all__'


class ChemoMedRecordForm (SubjectModelFormMixin):

    class Meta:
        model = ChemoMedRecord
        fields = '__all__'


class HaartRecordForm (SubjectModelFormMixin):

    class Meta:
        model = HaartRecord
        fields = '__all__'


class HaartMedRecordForm (SubjectModelFormMixin):

    class Meta:
        model = HaartMedRecord
        fields = '__all__'
