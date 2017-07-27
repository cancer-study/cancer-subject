from edc_visit_schedule.view_mixins import (
    VisitScheduleViewMixin as BaseVisitScheduleViewMixin)


class VisitScheduleViewMixin(BaseVisitScheduleViewMixin):

    def is_current_enrollment_model(self, enrollment_instance,
                                    schedule=None, **kwargs):
        if (enrollment_instance.schedule_name == 'schedule1'):
            return True
        return False
