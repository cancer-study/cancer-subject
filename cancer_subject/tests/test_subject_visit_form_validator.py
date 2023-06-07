import unittest

from django import forms
from edc_base import get_utcnow
from edc_constants.constants import YES
from edc_facility.import_holidays import import_holidays
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy

from cancer_subject.forms import SubjectVisitForm
from cancer_subject.forms.subject_visit_form import VisitFormValidator
from cancer_subject.models import Appointment, SubjectVisit
from cancer_subject.tests.models import DeathReport


class TestSubjectVisitFormValidator(unittest.TestCase):

    def setUp(self):
        import_holidays()
        death_model = 'cancer_subject.deathreport'
        VisitFormValidator.death_model = death_model
        self.consent = mommy.make_recipe(
            'cancer_subject.subjectconsent',
            consent_datetime=get_utcnow())
        options = {
            'subject_identifier': self.consent.subject_identifier,
            'has_diagnosis': YES,
            'enrollment_site': 'gaborone_private_hospital'}
        mommy.make_recipe(
            'cancer_subject.subjectscreening', **options)

        self.appointments = Appointment.objects.filter(
            subject_identifier=self.consent.subject_identifier)

        self.subject_identifier = self.consent.subject_identifier
        self.death_cls = DeathReport
        self.death_cls.objects.create(subject_identifier=self.subject_identifier, )
        self.data = {'subject_identifier': self.subject_identifier, 'appointment':
            self.appointments[0]}

    def test_validate_no_death_obj_raises_error(self):
        form = VisitFormValidator(cleaned_data=self.data)
        with self.assertRaises(forms.ValidationError) as cm:
            form.validate_no_death_obj()
        expected_error = ['You cannot start a new appointment if the participant is dead!']

        self.assertEqual(cm.exception.messages, expected_error)

    def test_validate_no_death_obj_passes(self):
        self.data['subject_identifier'] = '67890'
        form = VisitFormValidator(cleaned_data=self.data)
        form.validate_no_death_obj()  # should not raise any error

    def test_validate_no_death_visit_raises_error(self):
        form = VisitFormValidator(cleaned_data=self.data)
        self.death_visit = SubjectVisit.objects.create(
            reason='Death', subject_identifier=self.subject_identifier,
            appointment=self.appointments[0])
        self.death_visit.save()
        with self.assertRaises(forms.ValidationError) as cm:
            form.validate_no_death_visit()
        expected_error = ['You cannot start a new visit if the participant is dead!']

        self.assertEqual(cm.exception.messages, expected_error)

    def test_validate_no_death_visit_passes(self):
        self.death_visit = SubjectVisit.objects.create(
            reason=SCHEDULED, subject_identifier=self.subject_identifier,
            appointment=self.appointments[0])
        form = VisitFormValidator(cleaned_data=self.data)
        form.validate_no_death_visit()  # should not raise any error
