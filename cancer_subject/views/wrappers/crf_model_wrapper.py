from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper


class CrfModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'cancer_subject').admin_site_name
    next_url_name = django_apps.get_app_config(
        'cancer_subject').dashboard_url_name
    next_url_attrs = ['appointment', 'subject_identifier']
    querystring_attrs = ['subject_visit']

    @property
    def subject_visit(self):
        return self.object.subject_visit.id

    @property
    def appointment(self):
        return self.object.subject_visit.appointment.id
