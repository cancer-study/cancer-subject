from django.test import TestCase, tag
from model_mommy import mommy

from ambition_rando.import_randomization_list import import_randomization_list
from edc_base.utils import get_utcnow
from edc_constants.constants import YES
from edc_metadata.constants import NOT_REQUIRED, REQUIRED
from edc_metadata.models import CrfMetadata
from edc_visit_tracking.constants import SCHEDULED

from ..models import Appointment


class TestSubjectRules(TestCase):

    def setUp(self):
        import_randomization_list(verbose=False)
        screening = mommy.make_recipe('ambition_subject.subjectscreening',
                                      report_datetime=get_utcnow())
        self.consent = mommy.make_recipe(
            'ambition_subject.subjectconsent',
            consent_datetime=get_utcnow(),
            screening_identifier=screening.screening_identifier)

        self.visit_code = '1070'

        for appointment in Appointment.objects.all().order_by('timepoint'):
            self.subject_visit = mommy.make_recipe(
                'ambition_subject.subjectvisit',
                appointment=appointment,
                reason=SCHEDULED)
            if appointment.visit_code == self.visit_code:
                break

    def test_death_report_required_included_in_error(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_severity_grade='grade_5')

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_protocol_deviation_violation_required_included_in_error(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.studyterminationconclusion',
            subject_visit=self.subject_visit,
            termination_reason='included_in_error')

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_blood_result_required_prn_form(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.bloodresult',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            blood_result=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.bloodresult',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_adverse_event_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseevent',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_adverse_event_tmg_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventtmg',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event_tmg=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventtmg',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_adverse_event_followup_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventfollowup',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            adverse_event_followup=YES)

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.adverseeventfollowup',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_microbiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            microbiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.microbiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_radiology_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            radiology=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.radiology',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_lumbar_puncture_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            lumbar_puncture=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.lumbarpuncturecsf',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_recurrence_symptom_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            recurrence_symptom=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.recurrencesymptom',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_protocol_deviation_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            protocol_deviation=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.protocoldeviationviolation',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_death_report_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            death_report=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_death_report_tmg1_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreporttmg1',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            death_report_tmg1=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreporttmg1',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_death_report_tmg2_required(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreporttmg2',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)
        mommy.make_recipe(
            'ambition_subject.prnmodel',
            subject_visit=self.subject_visit,
            death_report_tmg2=YES)
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreporttmg2',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)

    def test_death_report_required_from_adverse_event(self):
        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            NOT_REQUIRED)

        mommy.make_recipe(
            'ambition_subject.adverseevent',
            subject_visit=self.subject_visit,
            ae_severity_grade='grade_5')

        self.assertEqual(
            CrfMetadata.objects.get(
                model='ambition_subject.deathreport',
                subject_identifier=self.consent.subject_identifier,
                visit_code='1070').entry_status,
            REQUIRED)
