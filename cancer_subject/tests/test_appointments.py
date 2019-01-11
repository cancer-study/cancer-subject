from django.test import TestCase, tag
from edc_appointment.constants import UNSCHEDULED_APPT, IN_PROGRESS_APPT
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_facility.import_holidays import import_holidays
from edc_visit_tracking.constants import UNSCHEDULED
from model_mommy import mommy

from ..models import Appointment


class TestSubjectConsent(TestCase):

    def setUp(self):
        import_holidays()

        options = {
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'cancer_subject.subjectconsent', **options)
        self.subject_identifier = consent.subject_identifier
        options = {
            'subject_identifier': self.subject_identifier,
            'has_diagnosis': YES,
            'enrollment_site': 'gaborone_private_hospital'}
        mommy.make_recipe(
            'cancer_subject.subjectscreening', **options)

    def test_appointments_creation(self):
        """Assert appointment triggering method creates appointments.
        """
        appointments = Appointment.objects.filter(
            subject_identifier=self.subject_identifier)
        self.assertEqual(appointments.count(), 21)

    @tag('visit')
    def test_visit_reason_unscheduled(self):
        """Test unscheduled visit creation"""
        appointment = Appointment.objects.get(visit_code=1000)
        appointment.appt_reason = UNSCHEDULED_APPT
        appointment.appt_status = IN_PROGRESS_APPT
        appointment.save()
        mommy.make_recipe(
            'cancer_subject.subjectvisit',
            appointment=appointment,
            reason=UNSCHEDULED)
        self.assertEqual(
            Appointment.objects.filter(
                visit_code=1000, visit_code_sequence=1).count(), 0)
