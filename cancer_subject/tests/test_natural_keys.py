from django.test import TestCase, tag
from model_mommy import mommy

from ambition_rando.import_randomization_list import import_randomization_list
from edc_base.utils import get_utcnow
from edc_metadata.tests import CrfTestHelper
from edc_sync.tests import SyncTestHelper
from edc_visit_tracking.constants import SCHEDULED

from ..models import Appointment


class TestNaturalKey(TestCase):

    sync_test_helper = SyncTestHelper()
    crf_test_helper = CrfTestHelper()

    def test_natural_key_attrs(self):
        self.sync_test_helper.sync_test_natural_key_attr(
            'ambition_subject')

    def test_get_by_natural_key_attr(self):
        self.sync_test_helper.sync_test_get_by_natural_key_attr(
            'ambition_subject')

    def complete_subject_visit(self):
        import_randomization_list(verbose=False)
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        consent = mommy.make_recipe('ambition_subject.subjectconsent',
                                    consent_datetime=get_utcnow(),
                                    screening_identifier=screening.screening_identifier)
        self.subject_identifier = consent.subject_identifier
        self.subject_visit = mommy.make_recipe(
            'ambition_subject.subjectvisit',
            appointment=Appointment.objects.get(
                subject_identifier=self.subject_identifier, visit_code='1000'),
            subject_identifier=consent.subject_identifier,
            reason=SCHEDULED,)
        return self.subject_visit

    def test_sync_test_natural_keys(self):
        complete_required_crfs = {}
        visit = self.complete_subject_visit()
        complete_required_crfs.update({
            visit.visit_code: self.crf_test_helper.complete_required_crfs(
                visit_code=visit.visit_code,
                visit=visit,
                subject_identifier=visit.subject_identifier)
        })
        self.sync_test_helper.sync_test_natural_keys(
            complete_required_crfs, verbose=True)
