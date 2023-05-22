from dateutil.tz import gettz
from django.apps import apps as django_apps
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents
from edc_constants.constants import FEMALE, MALE

from cancer_subject.consent_object_validator import ConsentObjectValidator

edc_protocol = django_apps.get_app_config('edc_protocol')

tzinfo = gettz('Africa/Gaborone')

v1 = Consent(
    'cancer_subject.subjectconsent',
    version='1',
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,
    age_min=18,
    age_is_adult=18,
    age_max=120,
    gender=[MALE, FEMALE])

v3 = Consent(
    'cancer_subject.subjectconsent',
    version='3',
    start=edc_protocol.study_open_datetime,
    end=edc_protocol.study_close_datetime,
    age_min=18,
    age_is_adult=18,
    age_max=120,
    gender=[MALE, FEMALE])

site_consents.validator_cls = ConsentObjectValidator

site_consents.register(v1)
site_consents.register(v3)
