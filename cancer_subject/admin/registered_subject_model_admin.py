from edc.subject.registration.admin import BaseRegisteredSubjectModelAdmin


class RegisteredSubjectModelAdmin (BaseRegisteredSubjectModelAdmin):

    """ModelAdmin subclass for models with a ForeignKey to 'registered_subject'"""

    dashboard_type = 'subject'
