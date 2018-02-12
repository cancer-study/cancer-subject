from django.utils.translation import ugettext_lazy as _
from edc_constants.constants import DONT_KNOW, NONE, NOT_SURE, DECLINED
from edc_constants.constants import NEG, IND, UNK, OTHER, NEVER
from edc_constants.constants import YES, NO, DWTA, NOT_APPLICABLE, POS

from cancer_subject.constants import (ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY,
                                      REFUSED, ALONE, NOT_PERFORMED, DAYS, MONTHS,
                                      YEARS, MARRIED, ZERO)


AGE_FIRSTSEX_CHOICE = (
    ('younger_than_15_years_old', 'younger than 15 years old'),
    ('between_15_and_17_years_old', 'between 15 and 17 years old'),
    ('older_than_17_years_old', 'older than 17 years old'),
    (DONT_KNOW, 'don\'t know'),
    ('never', 'never'),
    (DWTA, 'Don\'t want to answer'),
    (DECLINED, 'Patient declined to answer'),
)

ARV_REASON_CHOICE = (
    ('1', '1 = Treatment'),
    ('2', '2 = PMTCT'),
    ('3', '3 = PEP '),
)

BASIS_CHOICE = (
    (UNK, 'Unknown'),
    ('clinical', 'Clinical'),
    ('pathology', 'Pathology'),
)

BODILY_PAIN_CHOICE = (
    ('none', 'None'),
    ('very_mild', 'Very mild'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
    ('very_severe', 'Very serere'),
)

CANCER_BEFORE_CHOICE = (
    (DONT_KNOW, 'Don\'t know'),
    ('cervical_cancer', 'Cervical cancer'),
    ('breast_cancer', 'Breast cancer'),
    ('esophageal_cancer', 'Esophageal cancer'),
    ('Kaposi\'s_sarcoma', 'Kaposi\'s sarcoma'),
    ('lymphoma', 'Lymphoma'),
    ('leukemia', 'Leukemia'),
    ('Wilm\'s_Tumor', 'Wilm\'s Tumor'),
    (OTHER, ' Other or multiple cancers, describe:'),
)

CANCER_CATEGORY_CHOICE = (
    ('new', 'New Cancer (no treatment for this cancer type for >5 year,'
     ' or treatment began less than 6 weeks ago'),
    ('relapsed', 'Relapsed or recurrent cancer (no active treatment for'
     ' this cancer for >1 year)'),
    ('ongoing', 'Ongoing treatment (active treatment for this cancer'
     ' type in past year)'),
)

CANCER_TYPE_CHOICE = (
    (DONT_KNOW, 'Don\'t know'),
    ('cervical_cancer', 'Cervical cancer'),
    ('breast_cancer', 'Breast cancer'),
    ('esophageal_cancer', 'Esophageal cancer'),
    ('Kaposi\'s_sarcoma', 'Kaposi\'s sarcoma'),
    ('lymphoma', 'Lymphoma'),
    ('liver_cancer', 'Liver cancer'),
    ('eye_cancer', 'Eye cancer'),
    ('other_or_multiple_cancers',
     'Other or multiple cancers, describe:'),
)

CIGARETTE_SMOKING_CHOICE = (
    ('14_or_fewer_cigarettes_daily', '14 or fewer cigarettes a day'),
    ('between_15_and_25 cigarettes_daily', 'between 15 and 25 cigarettes a day'),
    ('more_than_25_cigarettes_daily', 'more than 25 cigarettes a day'),
    ('refused', 'Participant declined to answer')
)

COMMUNITY = (
    ('040', '040 Gaborone'),
    ('060', '060 Francistown'),
)

DIAGNOSIS_BASIS_CHOICE = (
    ('clinica_only', 'Clinical Only'),
    ('clinical_and_radiology', 'Clinical AND Radiology (CT, X-ray, U/S)'),
    ('surgery', 'Surgery'),
    ('biochemical/immunological_test', 'Biochemical/Immunological Test'),
    ('cytology/haematology', 'Cytology/Haematology'),
    ('histology_of_metastasis', 'Histology of Metastasis'),
    ('histology_of_primary', 'Histology of Primary'),
    ('autopsy_with_histology', 'Autopsy with Histology'),
    (OTHER, 'Other (including unknown): '),
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

DURATION_CHOICE = (
    ('<5_years', 'less than 5 years'),
    ('5_to_20 years', 'between 5 and 20 years'),
    ('>20_years', 'more than 20 years'),
)

EDUCATION_CHOICE = (
    (NONE, 'None'),
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
    (NONE, 'None'),
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

FOOD_SECURITY = (
    (NEVER, 'Never'),
    ('Rarely', 'Rarely'),
    ('Sometimes', 'Sometimes'),
    ('Often', 'Often'),
    (DECLINED, 'Patient declined to answer')
)

FREQUENCY_CHOICE = (
    ('never', 'never'),
    ('rarely', 'rarely'),
    ('sometimes', 'sometimes'),
    ('often', 'often'),
    ('always', 'always'),
)

FUEL_CHOICE = (
    ('solid_fuels', 'solid fuels (dung, charcoal, wood, crops, coal)'),
    ('kerosene_or_gas', 'kerosene or gas'),
    ('electricity', 'electricity'),
    (DONT_KNOW, 'don\'t know'),
    (OTHER, 'Other, specify:'),
)

HAART_MEDS_DRUG_NAMES = (
    ('ATR', 'Atripla (ATR)'),
    ('CBV', 'Combivir (CBV)'),
    ('EFV', 'Efavirenz (EFV)'),
    ('NVP', 'Nevirapine (NVP)'),
    ('3TC', 'Lamivudine (3TC)'),
    ('FTC', 'Emtricitabine (FTC)'),
    ('AZT_ZDV', 'Zidovudine (AZT or ZDV)'),
    ('TDF', 'Tenofovir (TDF)'),
    ('ABC', 'Abacavir (ABC)'),
    ('D4T', 'Stavudine (D4T)'),
    ('DDI', 'Didanosine (DDI)'),
    ('ALU', 'Aluvia/Kaletra (ALU)'),
    ('DRV', 'Darunavir (DRV)'),
    ('RAL', 'Raltegravir (RAL)'),
    ('OTHER', 'Other, specify')
)

HAART_STATUS_CHOICE = (
    ('never_started_HAART', 'Never started HAART "(skip to Question 4)"'),
    ('Follow_up_visit', 
     ' Follow-up visit, no modifications since last visit made to '
     'HAART treatment "(skip to Question 4)"'),
    ('enrollment_visit', ' Enrollment visit, patient has taken or '
     'is taking HAART "(go to Question 3, record all current and '
     'past HAART medications)"'),
    ('change_in_at_least_one_antiretroviral_medication',
     ' Change in at least one antiretroviral medication (dose '
     'modification, discontinuation, temporary hold, change of '
     'medication) "(go to Question 3)"'),
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

HEPATITIS_BEFORE_CHOICE = (
    ('no', 'No'),
    ('hepatitis_B', 'Hepatitis B'),
    ('hepatitis_C', 'Hepatitis C'),
    (DONT_KNOW, 'Don\'t know'),
)

HOURS_OUTDOOR_CHOICE = (
    ('1_hour_or_less', '1 hour or less'),
    ('2_hours', '2 hours'),
    ('3_hours', '3 hours'),
    ('4_hours', '4 hours'),
    ('5_hours', '5 hours'),
    ('6_hours', '6 hours'),
)

MARITAL_STATUS_CHOICE = (
    ('single', 'Single'),
    ('married', 'Married'),
    ('cohabiting', 'Cohabiting'),
    ('widowed', 'Widowed'),
    ('divorced', 'Divorced'),
    (OTHER, 'Other, specify:'),
)

METASTASIS_POSSIBLE_GRADES = (
    (UNK, 'Unknown'),
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
)

MINE_TYPE_CHOICE = (
    ('gold', 'gold'),
    ('diamond', 'diamond'),
    ('copper', 'copper'),
    ('nickel', 'nickel'),
    (OTHER, 'Other, specify:'),
)

MOD_REASON_CHOICE = (
    ('11', '11 = Initiation (or re-initiation after non-adherence/stockout)'),
    ('12', '12 = Toxicity decreased/resolved'),
    ('13', '13 = Vomiting'),
    ('14', '14 = CNS symptoms (sleep,psych, etc)'),
    ('15', '15 = Diarrhea'),
    ('16', '16 = Hypersensitivity/allergic reaction'),
    ('17', '17 = Hepatotoxicity'),
    ('18', '18 = Neutropenia'),
    ('19', '19 = Anemia'),
    ('20', '20 = Renal failure20 = Renal failure'),
    ('21', '21 = Other toxicity (specify in comments)'),
    ('22', '22 = Virologic failure'),
    ('23', '23 = Immunologic failure (CD4)'),
    ('24', '24 = Clinical failure'),
    ('25', '25 = Non-adherence'),
    ('26', '26 = Interaction with cancer treatment'),
    ('27', '27 = Death'),
    ('28', '28 = Other (specify in comments) '),
)

MONEY_EARNED_CHOICE = (
    (NONE, 'None'),
    ('<P200/month (P50/week)', '<P200/month (&lt; P50/week)'),
    ('P200-500/month (P50-120/week)', 'P200-500/month (P50-120/week)'),
    ('P501-1000/month (P120-230/week)', 'P501-1000/month (P120-230/week)'),
    ('P1001-2500/month (P230-580/week)', 'P1001-2500/month (P230-580/week)'),
    ('P2501-5000/month (P580-1160/week)', 'P2501-5000/month (P580-1160/week)'),
    ('P5001-10000/month (P1160-2330/week)', 'P5001-10000/month (P1160-2330/week)'),
    ('P10001-20000/month (P2330-4600/week)',
     'P10001-20000/month (P2330-4600/week)'),
    ('P20001-30000/month (P4600-7000/week)',
     'P20001-30000/month (P4600-7000/week)'),
    ('>P30000/month (>P7000/week)', '>P30000/month (>P7000/week)'),
)

MONEY_PROVIDED_CHOICE = (
    ('unsure', 'Unsure'),
    ('you', 'You'),
    ('partner', 'Partner or spouse'),
    ('parents', 'Parents'),
    ('relatives', 'Other relatives'),
    ('friend', 'Friend'),
    (OTHER, 'Other, specify:'),
)

OCCUPATION_CHOICE = (
    ('housewife', 'Housewife'),
    ('salaried_(govt)', 'Salaried (government)'),
    ('salaried_(private)', 'Salaried (private)'),
    ('domestic_work_(paid)', 'Domestic work (paid)'),
    ('self_employed', 'Self-employed'),
    ('student', 'Student'),
    ('unemployed', 'Unemployed'),
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

POSSIBLE_GRADES = (
    (UNK, 'Unknown'),
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

POSSIBLE_OVERALL_STAGES = (
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)

# Only two stages A and B
POSSIBLE_OVERALL_STAGE_MODIFIER = (
    (UNK, 'Unknown'),
    ('No stage modifier', 'No stage modifier'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

PROBS_FROM_WORK_CHOICE = (
    ('not_at_all', 'Not at all'),
    ('very_little', 'Very little'),
    ('somewhat', 'Somewhat'),
    ('quite_a_lot', 'Quite a lot'),
    ('no_daily_ activities', 'Could not do daily activities'),
)

QUIT_CHOICE = (
    ('less_than_2_years_ago', 'less than 2 years ago'),
    ('between_2_and_10_years_ago', 'between 2 and 10 years ago'),
    ('between_10_and_20_years_ago', 'between 10 and 20 years ago'),
    ('more_than_20_years_ago', 'more than 20 years ago'),
    ('refused', 'Participant declined to answer')
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

SMOKE_NOW_CHOICE = (
    (YES, YES),
    (NO, 'no, I used to smoke but quit'),
)

SYMPTOM_PROMPT_CHOICE = (
    ('pain', 'Pain'),
    ('lump/mass', 'Lump/Mass'),
    ('fever', 'Fever'),
    ('cough', 'Cough'),
    ('shortness_of_breath', 'Shortness of Breath'),
    ('bleeding', 'Bleeding'),
    ('weight_loss', 'Weight loss'),
    ('swelling_of_leg', 'Swelling of leg'),
    ('difficulty_swallowing', 'Difficulty swallowing'),
    ('bump/rash_on_skin_or_eye', 'Bump/rash on skin or eye'),
    (OTHER, 'Other, specify:'),
)

TB_TREATMENT_CHOICE = (
    (NO, 'No'),
    ('Yes_(IPT)', 'Yes, isoniazid preventative therapy (IPT)'),
    ('Yes_(ATT)', 'Yes, combination anti-tuberculosis treatment (ATT)'),
)

TEST_RESULT_CHOICE = (
    ('POS', 'Reactive'),
    ('NEG', 'Non-Reactive'),
)

TOILET_CHOICE = (
    ('indoor_toilet', 'Indoor toilet'),
    ('private_latrine', 'Private latrine for your house/compound'),
    ('shared_latrine', 'Shared latrine with other compounds'),
    ('no_latrine', 'No latrine facilities'),
    (OTHER, 'Other, specify:'),
)

TRADMEDICINE_CHOICE = (
    (NEVER, 'Never'),
    ('less_than_once_yearly', 'Less than once a year'),
    ('between_1_and_5_times_yearly', 'Between 1 and 5 times a year'),
    ('between_5_to_10_times_yearly', 'Between 5 to 10 times a year'),
    ('more_than_10_times_yearly', 'More than 10 times a year'),
    (DECLINED, 'Patient declined to answer'),
)

WHO_STAGE_CHOICE = (
    ('wasting', 'Wasting'),
    ('TB', 'Tuberculosis'),
    ('KS', 'Kaposi\'s sarcoma'),
    ('kidney_failure', 'Kidney failure'),
    ('CM', 'Cryptococcal meningitis'),
    ('severe_bacterial_infections', 'Severe bacterial infections'),
    (OTHER, 'Other, specify:'),
)

YES_NO_DECLINED = (
    (YES, YES),
    (NO, NO),
    (DECLINED, 'Patient declined to answer')
)