from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO
from edc_facility.import_holidays import import_holidays
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy

from ..models import Appointment, SubjectVisit, ResultsToRecord


@tag('rule')
class TestSubjectRules(TestCase):

    def setUp(self):
        import_holidays()
        self.consent = mommy.make_recipe(
            'cancer_subject.subjectconsent',
            consent_datetime=get_utcnow())
        options = {
            'subject_identifier': self.consent.subject_identifier,
            'has_diagnosis': YES,
            'enrollment_site': 'gaborone_private_hospital'}
        mommy.make_recipe(
            'cancer_subject.subjectscreening', **options)

        appointments = Appointment.objects.filter(
            subject_identifier=self.consent.subject_identifier)
        self.assertEqual(appointments.count(), 21)

        mommy.make_recipe(
            'cancer_subject.subjectvisit',
            appointment=Appointment.objects.get(visit_code='1000'),
            reason=SCHEDULED)

    def test_radiationtreatment_required(self):
        subject_visit = SubjectVisit.objects.get(visit_code=1000)
        mommy.make_recipe(
            'cancer_subject.oncologytreatmentplan',
            subject_visit=subject_visit,
            radiation_plan=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='cancer_subject.radiationtreatment',
                subject_identifier=self.consent.subject_identifier,
                visit_code=1000).entry_status, REQUIRED)

    def test_radiationtreatment_not_required(self):
        subject_visit = SubjectVisit.objects.get(visit_code=1000)
        mommy.make_recipe(
            'cancer_subject.oncologytreatmentplan',
            subject_visit=subject_visit,
            radiation_plan=NO)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='cancer_subject.radiationtreatment',
                subject_identifier=self.consent.subject_identifier,
                visit_code=1000).entry_status, NOT_REQUIRED)

    @tag('r1')
    def test_lab_result_haematology_required(self):
        subject_visit = SubjectVisit.objects.get(visit_code=1000)
        ResultsToRecord.objects.create(
            name='Haematology')

        options = {'subject_visit': subject_visit,
                   'results_to_record': ResultsToRecord.objects.all()}
        cancer_diagnosis = mommy.make_recipe(
            'cancer_subject.cancerdiagnosis', **options)
        cancer_diagnosis.results_to_record.set(ResultsToRecord.objects.all())
        cancer_diagnosis.save()

        self.assertEqual(
            CrfMetadata.objects.get(
                model='cancer_subject.labresulthaematology',
                subject_identifier=self.consent.subject_identifier,
                visit_code=1000).entry_status, REQUIRED)

    @tag('r1')
    def test_lab_result_haematology_not_required(self):
        subject_visit = SubjectVisit.objects.get(visit_code=1000)
        ResultsToRecord.objects.create(
            name='blah!')

        mommy.make_recipe(
            'cancer_subject.cancerdiagnosis',
            subject_visit=subject_visit,
            results_to_record=ResultsToRecord.objects.all())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='cancer_subject.labresulthaematology',
                subject_identifier=self.consent.subject_identifier,
                visit_code=1000).entry_status, NOT_REQUIRED)

    @tag('r1')
    def test_lab_result_chemistry_required(self):
        subject_visit = SubjectVisit.objects.get(visit_code=1000)
        ResultsToRecord.objects.create(
            name='Chemistry')

        cancer_diagnosis = mommy.make_recipe(
            'cancer_subject.cancerdiagnosis',
            subject_visit=subject_visit)
        cancer_diagnosis.results_to_record.set(ResultsToRecord.objects.all())
        cancer_diagnosis.save()

        self.assertEqual(
            CrfMetadata.objects.get(
                model='cancer_subject.labresultchemistry',
                subject_identifier=self.consent.subject_identifier,
                visit_code=1000).entry_status, REQUIRED)

    @tag('r1')
    def test_lab_result_chemistry_not_required(self):
        subject_visit = SubjectVisit.objects.get(visit_code=1000)
        ResultsToRecord.objects.create(name='None')

        mommy.make_recipe(
            'cancer_subject.cancerdiagnosis',
            subject_visit=subject_visit,
            results_to_record=ResultsToRecord.objects.all())

        self.assertEqual(
            CrfMetadata.objects.get(
                model='cancer_subject.labresultchemistry',
                subject_identifier=self.consent.subject_identifier,
                visit_code=1000).entry_status, NOT_REQUIRED)
