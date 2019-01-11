from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import YES, NO
from edc_facility.import_holidays import import_holidays
from edc_metadata.constants import REQUIRED, NOT_REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy

from ..models import Appointment
from ..models import SubjectVisit


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

        for appointment in Appointment.objects.all().order_by('timepoint'):
            mommy.make_recipe(
                'cancer_subject.subjectvisit',
                appointment=appointment,
                reason=SCHEDULED)

    @tag('rule')
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

    @tag('rule')
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
