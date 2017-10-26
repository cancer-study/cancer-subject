from ..forms import PatientHistoryForm
from ..models import Appointment
from ambition_rando.import_randomization_list import import_randomization_list
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import NO, YES, NOT_APPLICABLE
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


@tag('ph')
class TestPatientHistoryFormValidator(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')

        options = {
            'screening_identifier': subject_screening.screening_identifier,
            'consent_datetime': get_utcnow, }
        consent = mommy.make_recipe(
            'ambition_subject.subjectconsent', **options)
        self.subject_identifier = consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code='1000'),
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)

    def test_tb_history_yes_tb_site_none_invalid(self):
        options = {'care_before_hospital': NO,
                   'subject_visit': self.subject_visit,
                   'report_datetime': get_utcnow()}
#                    'medicalexpenses_set-0-location_care': NOT_APPLICABLE}

        patient_history = mommy.make_recipe(
            'ambition_subject.patienthistory', **options)
        form = PatientHistoryForm()
        print(">>>>>>>>", form.errors)
        self.assertTrue(form.is_valid())
#         form = PatientHistoryForm(cleaned_data=cleaned_data)
#         self.assertRaises(ValidationError, form.validate)
#         self.assertIn('tb_site', form._errors)
