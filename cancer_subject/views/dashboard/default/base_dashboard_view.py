from edc_metadata.view_mixins import MetaDataViewMixin

from edc_subject_dashboard.view_mixins import (
    ConsentViewMixin, ShowHideViewMixin, SubjectIdentifierViewMixin)


from ..appointment_view_mixin import AppointmentViewMixin
from ..subject_visit_view_mixin import SubjectVisitViewMixin
from ..visit_schedule_view_mixin import VisitScheduleViewMixin


class BaseDashboardView(
        MetaDataViewMixin,
        ConsentViewMixin,
        SubjectVisitViewMixin,
        AppointmentViewMixin,
        VisitScheduleViewMixin,
        ShowHideViewMixin,
        SubjectIdentifierViewMixin):
    pass
