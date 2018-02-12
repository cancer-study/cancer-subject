from django.utils.translation import ugettext_lazy as _
from edc_constants.constants import DONT_KNOW, NONE, NOT_SURE, DECLINED
from edc_constants.constants import NEG, IND, UNK, OTHER
from edc_constants.constants import YES, NO, DWTA, NOT_APPLICABLE, POS

from cancer_subject.constants import (ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY,
                                      REFUSED, ALONE, NOT_PERFORMED, DAYS, MONTHS,
                                      YEARS, MARRIED, ZERO)

BODILY_PAIN_CHOICE = (
    ('none', 'None'),
    ('very_mild', 'Very mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
    ('very_severe', 'Very serere'),
)

DIFFICULTY_WORK_CHOICE = (
    ('none_at_all', 'None at all'),
    ('a_little_bit', 'A little bit'),
    ('some', 'Some'),
    ('quite_a_lot', 'Quite a lot'),
    ('no_daily_work', 'Could not do daily work'),
)

DISTRICT20_CHOICE = (
    ('Central', 'Central District'),
    ('Ghanzi', 'Ghanzi District'),
    ('Kgalagadi', 'Kgalagadi District'),
    ('Kgatleng', 'Kgatleng District'),
    ('Kweneng', 'Kweneng District'),
    ('North-East', 'North-East District '),
    ('North-West', 'North-West District (includes Chobe/Ngamiland)'),
    ('South-East', 'South-East District'),
    ('Southern', 'Southern District'),
)

EDUCATION_CHOICE = (
    ('none', 'None'),
    ('primary', 'Primary'),
    ('junior_secondary', 'Junior secondary'),
    ('senior_secondary', 'Senior secondary'),
    ('tertiary', 'Tertiary'),
)

EMOTIONAL_PROBS_CHOICE = (
    ('not_at_all', 'Not at all'),
    ('slightly', 'Slightly'),
    ('moderately', 'Moderately'),
    ('quite_a_lot', 'Quite a lot'),
    ('extremely', 'Extremely'),
)

ENERGY_CHOICE = (
    ('very_much', 'Very much'),
    ('quite_a_lot', 'Quite a lot'),
    ('some', 'Some'),
    ('a_little', 'A little'),
    ('none', 'None'),
)

ETHNIC_GRP_CHOICE = (
    ('Tswana_Bangwato', 'Tswana-Bangwato'),
    ('Tswana_Bakwena', 'Tswana-Bakwena'),
    ('Tswana_Bangwaketsi', 'Tswana-Bangwaketsi'),
    ('Tswana_Bakgatla', 'Tswana-Bakgatla'),
    ('Tswana_Batawana', 'Tswana-Batawana'),
    ('Tswana_Barolong', 'Tswana-Barolong'),
    ('Tswana_Bamalete', 'Tswana-Bamalete'),
    ('Tswana_Batlokwa', 'Tswana-Batlokwa'),
    ('Bakalanga', 'Bakalanga'),
    ('Basarwa', 'Basarwa'),
    ('Kgalagadi', 'Kgalagadi'),
    ('White', 'White'),
    ('Asian', 'Asian'),
    (OTHER, 'Other, specify:'),
)

HEALTH_PROBLEMS_CHOICE = (
    ('not_at_all', 'Not at all'),
    ('very_little', 'Very Little'),
    ('somewhat', 'Somewhat'),
    ('quite_a_lot', 'Quite a lot'),
    ('no_physical_activities', 'Could not do physical activities'),
)

HEALTH_PROBS_LIMIT_CHOICE = (
    ('not_at_all', 'Not at all'),
    ('very_little', 'Very little'),
    ('somewhat', 'Somewhat'),
    ('quite_a_lot', 'Quite a lot'),
    ('no_social_activities', 'Could not do social activities'),
)

HEALTH_RATE_CHOICE = (
    ('excellent', 'Excellent'),
    ('very_good', 'Very Good'),
    ('good', 'Good'),
    ('fair', 'Fair'),
    ('poor', 'Poor'),
    ('very_poor', 'Very Poor'),
)

MARITAL_STATUS_CHOICE = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('cohabiting', 'Cohabiting'),
    ('widowed', 'Widowed'),
    ('divorced', 'Divorced'),
    (OTHER, 'Other, specify:'),
)

OFF_STUDY_CODE_CHOICE = (
    ('completion_of_protocol_required_period_of_time_for_observation',
     'Completion of protocol required period of time for '
     'observation (see MOP for definition of Completion.)'),
    ('death',
     'Death (complete the AF005 Death Record form)'),
    ('participant_refused_further_contact',
     'Participant refused further contact (explain in Comments below)'),
    ('unable_to_contact_participant_despite_repeated_attempts',
     'Unable to contact Participant despite repeated attempts '
     '(see MOP for definition of Lost to Follow-Up.)'),
    (OTHER, 'Other, specify:'),
)

PERFORM_STATUS_CHOICE = (
    ('0', 'Asymptomatic (Fully active, able to carry on all pre-disease '
     'activities without restriction)'),
    ('1', 'Symptomatic but completely ambulatory (Restricted in physically '
     'strenuous activity but ambulatory and able to carry out work of a light '
     'or sedentary nature. For example, light housework, office work)'),
    ('2', 'Symptomatic, &lt;50% in bed during the day (Ambulatory and capable '
     'of all self care but unable to carry out any work activities. Up and '
     'about more than 50% of waking hours)'),
    ('3', '50% in bed, but not bedbound (Capable of only limited self-care, '
     'confined to bed or chair 50% or more of waking hours)'),
    ('4', 'Bedbound (Completely disabled. Cannot carry on any self-care. '
     'Totally confined to bed or chair)'),
)

PROBS_FROM_WORK_CHOICE = (
    ('not_at_all', 'Not at all'),
    ('very_little', 'Very little'),
    ('somewhat', 'Somewhat'),
    ('quite_a_lot', 'Quite a lot'),
    ('no_daily_ activities', 'Could not do daily activities'),
)

RACE_CHOICE = (
    ('black_african', 'Black African'),
    ('caucasian', 'Caucasian'),
    ('asian', 'Asian'),
    (OTHER, 'Other, specify:'),
)

RELATIONSHIP_DESCRIPTION_CHOICE = (
    ('definitely_related',
        'Definitely related to study activities'),
    ('probably_related',
        'Probably related to study activities'),
    ('possibly_related',
        ' Possibly related to study activities'),
    ('probably_NOT_related',
        ' Probably NOT related to study activities'),
    ('not_related',
     ' Not related to study activities'),
    ('pending,cannot_tell_yet_if_related',
     ' Pending, cannot tell yet if related to study activities'),
)

REPORT_TYPE_CHOICE = (
    ('original_report', 'Original report of an event'),
    ('updated_information', 'Updated information'),
    ('resolution', 'Resolution'),
)

SETTING_CHOICE = (
    ('farm/lands', 'Farm/lands'),
    ('village', 'Village'),
    ('city/town', 'City/Town'),
)

