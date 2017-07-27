from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper


class SubjectConsentModelWrapper(ModelWrapper):

    model = 'cancer_subject.subjectconsent'
    next_url_name = django_apps.get_app_config(
        'cancer_subject').dashboard_url_name
    next_url_attrs = ['subject_identifier', ]
    querystring_attrs = [
        'gender', 'subject_screening', 'first_name', 'initials', 'modified']

    @property
    def subject_screening(self):
        return str(self.object.subject_screening.id)

    @property
    def subject_identifier(self):
        return str(self.object.subject_identifier)
