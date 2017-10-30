from datetime import date

from django.apps import apps as django_apps
from django.test import TestCase
from edc_base.utils import get_utcnow
from edc_constants.constants import FEMALE, MALE, NO, YES
from edc_registration.models import RegisteredSubject

from cancer_subject.models import SubjectConsent, EnrollmentChecklist
from cancer_subject.models.appointment import Appointment
from edc_consent.consent import Consent
from edc_consent.site_consents import site_consents


class TestEnrollment(TestCase):

    def setUp(self):
        app_config = django_apps.get_app_config('edc_protocol')
        self.study_open_datetime = app_config.study_open_datetime
        self.study_close_datetime = app_config.study_close_datetime
        site_consents.backup_registry()
        self.consent_factory(
            start=self.study_open_datetime,
            end=self.study_close_datetime,
            version='1.0')
        self.options = dict(
            study_site='40',
            consent_datetime=get_utcnow(),
            dob=date(1980, 10, 1),
            first_name='TEST',
            last_name='TEST',
            initials='TT',
            gender='M',
            identity='12315678',
            confirm_identity='12315678',
            identity_type='OMANG',
            is_dob_estimated='-',
            is_incarcerated=NO)

    def consent_factory(self, **kwargs):
        options = dict(
            start=kwargs.get('start'),
            end=kwargs.get('end'),
            gender=kwargs.get('gender', [MALE, FEMALE]),
            updates_versions=kwargs.get('updates_versions', []),
            version=kwargs.get('version', '1'),
            age_min=kwargs.get('age_min', 16),
            age_max=kwargs.get('age_max', 64),
            age_is_adult=kwargs.get('age_is_adult', 18))
        model = kwargs.get('model', 'cancer_subject.subjectconsent')
        consent = Consent(model, **options)
        site_consents.register(consent)
        return consent

    def test_subject_consent(self):
        SubjectConsent.objects.create(
            **self.options)
        self.assertEqual(SubjectConsent.objects.all().count(), 1)

    def test_subject_consent_1(self):
        SubjectConsent.objects.create(**self.options)
        self.assertEqual(SubjectConsent.objects.all().count(), 1)
        self.assertEqual(RegisteredSubject.objects.all().count(), 1)
        reg = RegisteredSubject.objects.first()
        self.assertTrue(reg.subject_identifier)

    def test_subject_consent_2(self):
        consent = SubjectConsent.objects.create(
            **self.options)
        EnrollmentChecklist.objects.create(
            has_diagnosis=YES,
            enrollment_site='gaborone_private_hospital',
            subject_identifier=consent.subject_identifier
        )
        self.assertEqual(EnrollmentChecklist.objects.filter(
            subject_identifier=consent.subject_identifier).count(), 1)

    def test_subject_consent_3(self):
        consent = SubjectConsent.objects.create(
            **self.options)
        EnrollmentChecklist.objects.create(
            has_diagnosis=YES,
            enrollment_site='gaborone_private_hospital',
            subject_identifier=consent.subject_identifier
        )
        self.assertEqual(Appointment.objects.all().count(), 21)
