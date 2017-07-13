from django.apps import AppConfig as DjangoApponfig

from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig


class AppConfig(DjangoApponfig):
    name = 'cancer_subject'
    listboard_template_name = 'cancer_subject/listboard.html'
    dashboard_template_name = 'cancer_subject/dashboard.html'
    base_template_name = 'edc_base/base.html'
    listboard_url_name = 'cancer_subject:listboard_url'
    dashboard_url_name = 'cancer_subject:dashboard_url'
    admin_site_name = 'cancer_subject_admin'
    url_namespace = 'cancer_subject'


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    visit_models = {
        'cancer_subject': ('subject_visit', 'bcpp_clinic_subject.subjectvisit')}