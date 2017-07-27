from django.apps import apps as django_apps

from edc_model_wrapper import ModelWrapper


class RequisitionModelWrapper(ModelWrapper):

    model = 'cancer_subject.subjectrequisition'
    admin_site_name = django_apps.get_app_config(
        'cancer_subject').admin_site_name
    next_url_name = django_apps.get_app_config(
        'cancer_subject').dashboard_url_name
    next_url_attrs = ['appointment', 'subject_identifier']
    querystring_attrs = ['subject_visit', 'panel_name']

    @property
    def subject_visit(self):
        return self.object.subject_visit.id

    @property
    def appointment(self):
        return self.object.subject_visit.appointment.id
