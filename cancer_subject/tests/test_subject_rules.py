from django.test import TestCase, tag
from django.test.utils import override_settings
from edc_appointment.models import Appointment
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_facility.import_holidays import import_holidays
from edc_metadata.constants import REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED
from model_mommy import mommy


class TestSubjectRules(TestCase):

    def setUp(self):
        import_holidays()
        screening = mommy.make_recipe(
            'cancer_screening.subjectscreening',
            report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'cancer_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        for appointment in Appointment.objects.all().order_by('timepoint'):
            self.subject_visit = mommy.make_recipe(
                'cancer_subject.subjectvisit',
                appointment=appointment,
                reason=SCHEDULED)
            print('code:', self.subject_visit)

    @tag('rule')
    def test_1(self):
        pass
