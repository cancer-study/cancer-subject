
class SubjectVisitViewMixin:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject_visit = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            self.subject_visit = self.appointment.subjectvisit
        except AttributeError as e:
            if 'subjectvisit' not in str(e) and 'object' not in str(e):
                raise
        context.update(subject_visit=self.subject_visit)
        return context
