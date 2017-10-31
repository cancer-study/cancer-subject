from dateutil.relativedelta import relativedelta
from edc_base.utils import get_utcnow
from edc_constants.constants import NO
from faker import Faker
from faker.providers import BaseProvider
from model_mommy.recipe import Recipe, seq

from cancer_subject.models import SubjectConsent, SymptomsAndTesting
from edc_consent.tests import EdcConsentProvider
from edc_constants.choices import YES
from cancer_subject.patterns import subject_identifier


class DateProvider(BaseProvider):

    def next_month(self):
        return (get_utcnow() + relativedelta(months=1)).date()

    def last_year(self):
        return (get_utcnow() - relativedelta(years=1)).date()

    def three_months_ago(self):
        return (get_utcnow() - relativedelta(months=3)).date()

    def thirty_four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=34)).date()

    def four_weeks_ago(self):
        return (get_utcnow() - relativedelta(weeks=4)).date()

    def yesterday(self):
        return (get_utcnow() - relativedelta(days=1)).date()


fake = Faker()
fake.add_provider(DateProvider)
fake.add_provider(EdcConsentProvider)

subjectconsent = Recipe(
    SubjectConsent,
    subject_identifier=None,
    study_site='40',
    consent_datetime=get_utcnow(),
    dob=fake.dob_for_consenting_adult,
    first_name=fake.first_name,
    last_name=fake.last_name,
    initials=fake.initials,
    gender='M',
    identity=seq('12315678'),
    confirm_identity=seq('12315678'),
    identity_type='OMANG',
    is_dob_estimated='-',
    is_incarcerated=NO,)

symptomsandtesting = Recipe(
    SymptomsAndTesting,
    subject_identifier=None,
    symptom_prompt='bleeding',
    symptom_date=fake.last_month,
    medical_doctor_date=fake.last_month,
    trad_doctor_date=fake.last_month,
    facility_first_seen='00-0-00',
    facility_first_seen_other='Church',
    hiv_tested=YES,
    hiv_test_result='Refused',
    pos_date=fake.last_year,
    neg_date=fake.last_year,
    hiv_result='Pending',
    arv_art_therapy=YES,
)
