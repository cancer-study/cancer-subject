from .modelform_mixin import SubjectModelFormMixin
from ..models import ActivityAndFunctioning


class ActivityAndFunctioningForm (SubjectModelFormMixin):

    class Meta:
        model = ActivityAndFunctioning
        fields = '__all__'
