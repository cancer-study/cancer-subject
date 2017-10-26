from ambition_rando.import_randomization_list import import_randomization_list
from edc_base.utils import get_utcnow
from edc_pharma.models import DispenseAppointment
from edc_pharma.models import DispenseSchedule
from edc_pharma.models import Prescription
from edc_pharma.models import WorkList
from edc_visit_tracking.constants import SCHEDULED

from django.test import TestCase, tag
from model_mommy import mommy

from ..models import Appointment
from ..models import SubjectVisit


class TestSubjectDispenseSchedule(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        self.visit_code = '1000'
        self.appointment = Appointment.objects.all().order_by('timepoint').first()
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=self.appointment,
            reason=SCHEDULED)

    @tag('pre')
    def test_create_prescriptions_by_patienthistory(self):
        visit = SubjectVisit.objects.get(appointment=self.appointment)
        mommy.make_recipe(
            'ambition_subject.patienthistory',
            subject_visit=visit)
        self.assertEqual(DispenseSchedule.objects.filter(
            subject_identifier=self.consent.subject_identifier).count(), 2)
        self.assertEqual(Prescription.objects.all().count(), 9)
        self.assertEqual(WorkList.objects.filter(
            subject_identifier=visit.subject_identifier).count(), 1)

    def test_single_dose_schedule(self):
        """ Assert that dispense timepoints for single dose subject
        are created correctly. 
        """
        self.assertEqual(DispenseSchedule.objects.filter(
            subject_identifier=self.consent.subject_identifier).count(), 2)
        self.assertEqual(DispenseAppointment.objects.filter(
            schedule__name='schedule1',
            schedule__subject_identifier=self.consent.subject_identifier).count(), 2)
        self.assertEqual(DispenseAppointment.objects.filter(
            schedule__name='schedule2',
            schedule__subject_identifier=self.consent.subject_identifier).count(), 2)

    def test_single_dose_schedule1(self):
        """ Assert that dispense timepoints for single dose subject
        are created correctly on update of subject consent. 
        """
        self.consent.consent_datetime = get_utcnow()
        self.consent.save()
        self.assertEqual(DispenseSchedule.objects.filter(
            subject_identifier=self.consent.subject_identifier).count(), 2)
        self.assertEqual(DispenseAppointment.objects.filter(
            schedule__name='schedule1',
            schedule__subject_identifier=self.consent.subject_identifier).count(), 2)
        self.assertEqual(DispenseAppointment.objects.filter(
            schedule__name='schedule2',
            schedule__subject_identifier=self.consent.subject_identifier).count(), 2)

    @tag('single_dose')
    def test_single_dose_schedule2(self):
        """ Assert that dispense timepoints for single dose subject
        are created correctly on update of subject consent. 
        """
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)
        consent.save()

        self.assertEqual(DispenseSchedule.objects.filter(
            subject_identifier=consent.subject_identifier).count(), 2)
        self.assertEqual(DispenseAppointment.objects.filter(
            schedule__name='schedule1',
            schedule__subject_identifier=self.consent.subject_identifier).count(), 2)
        self.assertEqual(DispenseAppointment.objects.filter(
            schedule__name='schedule2',
            schedule__subject_identifier=self.consent.subject_identifier).count(), 2)
