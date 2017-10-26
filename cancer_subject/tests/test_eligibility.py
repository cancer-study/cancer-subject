from django.apps import apps as django_apps
from django.test import TestCase, tag
from edc_constants.constants import FEMALE, YES, MALE, ABNORMAL, NORMAL, NO
from model_mommy import mommy

from ..eligibility import (
    AgeEvaluator, GenderEvaluator, Eligibility, ConsentAbilityEvaluator,
    MentalStatusEvaluatorError)


@tag('screening')
class TestSubjectScreening(TestCase):

    def setUp(self):
        django_apps.app_configs[
            'cancer_subject'].screening_age_adult_upper = 99
        django_apps.app_configs[
            'cancer_subject'].screening_age_adult_lower = 18

    def test_eligibility_invalid_age_in_years(self):
        age_evaluator = AgeEvaluator(age=17)
        self.assertFalse(age_evaluator.eligible)
        age_evaluator = AgeEvaluator(age=18)
        self.assertTrue(age_evaluator.eligible)
        age_evaluator = AgeEvaluator(age=99)
        self.assertTrue(age_evaluator.eligible)
        age_evaluator = AgeEvaluator(age=100)
        self.assertFalse(age_evaluator.eligible)

    def test_eligibility_invalid_age_in_years_reasons(self):
        age_evaluator = AgeEvaluator(age=17)
        self.assertIn('age<18', age_evaluator.reason)
        age_evaluator = AgeEvaluator(age=100)
        self.assertIn('age>99', age_evaluator.reason)

    def test_eligibility_gender(self):
        gender_evaluator = GenderEvaluator()
        self.assertFalse(gender_evaluator.eligible)
        gender_evaluator = GenderEvaluator(gender=FEMALE, pregnant=False)
        self.assertTrue(gender_evaluator.eligible)
        gender_evaluator = GenderEvaluator(gender=MALE)
        self.assertTrue(gender_evaluator.eligible)

        gender_evaluator = GenderEvaluator(
            gender=FEMALE, pregnant=False, breast_feeding=True)
        self.assertFalse(gender_evaluator.eligible)

        gender_evaluator = GenderEvaluator(
            gender=FEMALE, pregnant=True, breast_feeding=False)
        self.assertFalse(gender_evaluator.eligible)

        gender_evaluator = GenderEvaluator(
            gender=FEMALE, pregnant=False, breast_feeding=False)
        self.assertTrue(gender_evaluator.eligible)

    def test_eligibility_gender_reasons(self):
        gender_evaluator = GenderEvaluator()
        self.assertIn('invalid gender', gender_evaluator.reason)
        gender_evaluator = GenderEvaluator(gender=FEMALE, pregnant=True)
        self.assertIn('pregnant', gender_evaluator.reason)
        gender_evaluator = GenderEvaluator(gender='DOG')
        self.assertIn('invalid gender', gender_evaluator.reason)
        gender_evaluator = GenderEvaluator(gender=MALE)
        self.assertIsNone(gender_evaluator.reason)

    def test_eligibility(self):
        obj = Eligibility(
            age=18, gender=FEMALE, pregnant=False,
            consent_ability=True,
            will_hiv_test=True,
            meningitis_dx=True,
            no_drug_reaction=True,
            no_concomitant_meds=True,
            no_amphotericin=True,
            no_fluconazole=True,
            mental_status=NORMAL)
        self.assertTrue(obj.eligible)
        self.assertIsNone(obj.reasons or None)

    def test_not_eligible(self):
        obj = Eligibility(
            age=18, gender=FEMALE, pregnant=False,
            mental_status=NORMAL,
            will_hiv_test=False,
            meningitis_dx=True,
            no_drug_reaction=True,
            no_concomitant_meds=True,
            no_amphotericin=False,
            no_fluconazole=True)
        self.assertFalse(obj.eligible)
        self.assertIsNotNone(obj.reasons)

    def test_eligibility_reasons(self):
        obj = Eligibility(
            age=18, gender=FEMALE,
            mental_status=ABNORMAL,
            consent_ability=False,
            will_hiv_test=False,
            pregnant=False)
        reasons = ['Previous adverse drug reaction to the study medication',
                   'Patient on Contraindicated Meds', 'Unable to consent.',
                   'Previous Hx of Cryptococcal Meningitis',
                   'HIV unknown, not willing to consent',
                   '> 0.7mg/kg of Amphotericin B', '> 48hrs of Fluconazole']
        reasons.sort()
        reasons1 = obj.reasons
        reasons1.sort()
        self.assertEqual(reasons, reasons1)

    def test_subject_eligible_with_mommy_default(self):
        """Asserts mommy recipe default criteria is eligible.
        """
        subject_screening = mommy.prepare_recipe(
            'ambition_subject.subjectscreening')
        self.assertTrue(subject_screening.eligible)

    def test_subject_invalid_age_in_years_lower(self):
        """Asserts mommy recipe default criteria is eligible.
        """
        subject_screening = mommy.prepare_recipe(
            'ambition_subject.subjectscreening', age_in_years=17)
        subject_screening.verify_eligibility()
        self.assertFalse(subject_screening.eligible)

    def test_subject_age_minor_invalid_reason(self):
        options = {'age_in_years': 17}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)
        self.assertIn(
            subject_screening.reasons_ineligible, 'age<18')

    def test_subject_age_valid_no_reason(self):
        options = {'age_in_years': 18}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertTrue(subject_screening.eligible)
        self.assertEqual(subject_screening.reasons_ineligible, '')

    def test_subject_ineligible_female_pregnant(self):
        """Assert not eligible if pregnant.
        """
        options = {'gender': FEMALE, 'pregnancy': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_previous_adverse_drug_reaction(self):
        """Assert eligibility of a participant with a previous adverse
        drug reaction.
        """
        options = {'previous_drug_reaction': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_taking_concomitant_medication(self):
        """Test eligibility of a participant taking concomitant
        medication.
        """
        options = {'contraindicated_meds': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_took_two_days_amphotricin_b(self):
        """Test eligibility of a participant that received two days
        amphotricin_b before screening.
        """
        options = {'received_amphotericin': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_subject_ineligible_took_received_fluconazole(self):
        """Assert eligibility of a participant that received two days
        fluconazole before screening.
        """
        options = {'received_fluconazole': YES}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertFalse(subject_screening.eligible)

    def test_successful_screening_id_not_regenerated_on_resave(self):
        """Test subject screening id is not regenerated when resaving
           subject screening
        """
        options = {'age_in_years': 18}
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening', **options)
        self.assertTrue(subject_screening.eligible)
        screening_id = subject_screening.screening_identifier
        subject_screening.save()
        self.assertEqual(subject_screening.screening_identifier, screening_id)

    def test_mental_status_evaluator(self):
        status = ConsentAbilityEvaluator(
            mental_status=NORMAL, consent_ability=True)
        self.assertTrue(status.eligible)
        status = ConsentAbilityEvaluator(
            mental_status=ABNORMAL, consent_ability=True)
        self.assertTrue(status.eligible)
        status = ConsentAbilityEvaluator(
            mental_status=ABNORMAL, consent_ability=False)
        self.assertFalse(status.eligible)
        status = ConsentAbilityEvaluator(
            mental_status=NORMAL, consent_ability=False)
        self.assertFalse(status.eligible)
        self.assertRaises(
            MentalStatusEvaluatorError, ConsentAbilityEvaluator, mental_status='BLAH!')
        self.assertRaises(
            MentalStatusEvaluatorError, ConsentAbilityEvaluator, mental_status=None)

    def test_mental_status_reason(self):
        status = ConsentAbilityEvaluator(mental_status=ABNORMAL)
        self.assertIn(
            'Unable to consent.', status.reason)

    def test_eligible_mental_status_normal(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening')
        self.assertIn(subject_screening.mental_status, NORMAL)
        self.assertTrue(subject_screening.eligible)

    def test_ineligible_mental_abnormal(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            mental_status=ABNORMAL, consent_ability=NO)
        self.assertFalse(subject_screening.eligible)

    def test_ineligible_not_willing_to_hiv_test(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            will_hiv_test=NO)
        self.assertFalse(subject_screening.eligible)

    def test_eligible_willing_to_hiv_test(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            will_hiv_test=YES)
        self.assertTrue(subject_screening.eligible)

    def test_eligible_mental_abnormal_with_consent_ability(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            mental_status=ABNORMAL,
            consent_ability=YES)
        self.assertTrue(subject_screening.eligible)

    def test_ineligible_breastfeeding(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            gender=FEMALE, pregnancy=NO, breast_feeding=YES)
        self.assertFalse(subject_screening.eligible)

    def test_eligible_breastfeeding_recipe(self):
        subject_screening = mommy.make_recipe(
            'ambition_subject.subjectscreening',
            gender=FEMALE, pregnancy=NO, breast_feeding=NO)
        self.assertTrue(subject_screening.eligible)
