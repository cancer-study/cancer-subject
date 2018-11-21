import re

from django.test import TestCase, tag
from edc_appointment.models.appointment import Appointment
from edc_base.utils import get_utcnow
from edc_facility.import_holidays import import_holidays
from model_mommy import mommy


class TestSubjectConsent(TestCase):

    def setUp(self):
        import_holidays()
        subject_screening = mommy.make_recipe(
            'cancer_screening.subjectscreening')

        options = {
            'screening_identifier': subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'cancer_subject.subjectconsent', **options)
        self.subject_identifier = consent.subject_identifier

    def test_appointments_creation(self):
        """Assert appointment triggering method creates appointments.
        """
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_identifier)
        self.assertEqual(appointments.count(), 21)
