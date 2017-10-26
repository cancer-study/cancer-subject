from django.utils.translation import ugettext_lazy as _
from edc_constants.constants import DONT_KNOW, NONE, NOT_SURE, DECLINED
from edc_constants.constants import NEG, IND, UNK, OTHER
from edc_constants.constants import YES, NO, DWTA, NOT_APPLICABLE, POS

from cancer_subject.constants import ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY,\
    REFUSED, ALONE, NOT_PERFORMED, DAYS, MONTHS, YEARS, MARRIED, ZERO


VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology',
     'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'))

OFF_STUDY_CODE_CHOICE = (
    ('Completion of protocol required period of time for '
     'observation (see MOP for definition of Completion.)',
     'Completion of protocol required period of time for '
     'observation (see MOP for definition of Completion.)'),
    ('Death (complete the AF005 Death Record form)',
     'Death (complete the AF005 Death Record form)'),
    ('Participant refused further contact (explain in Comments below)',
     'Participant refused further contact (explain in Comments below)'),
    ('Unable to contact Participant despite repeated attempts '
     '(see MOP for definition of Lost to Follow-Up.)',
     'Unable to contact Participant despite repeated attempts '
     '(see MOP for definition of Lost to Follow-Up.)'),
    ('Other, specify: ', 'Other, specify: '),)


AGREE_STRONGLY = (
    ('Strongly disagree', _('Strongly disagree')),
    ('Disagree', _('Disagree')),
    ('Uncertain', _('Uncertain')),
    ('Agree', _('Agree')),
    ('Strongly agree', _('Strongly agree')),
    (DWTA, _('Don\'t want to answer')),
)

APPT_LOCATIONS = (
    ('home', 'At home'),
    ('work', 'At work'),
    ('clinic', 'At clinic'),
    (OTHER, 'Other location'),
)


APPT_GRADING = (
    ('firm', 'Firm appointment'),
    ('weak', 'Possible appointment'),
    ('guess', 'Estimated by RA'),
)

# BLOOD_DRAW_TYPES = (
#     (CAPILLARY, 'Capillary'),
#     (VENOUS, 'Venous'),
#     (NOT_APPLICABLE, 'Not applicable'),
# )

CHRONIC_DISEASES = (
    ('diabetes', 'Diabetes'),
    ('high_bp', 'High blood pressure'),
    ('mental_illness', 'Mental Illness'),
    (OTHER, 'Other'),
)

CONTACT_TYPE = (
    ('direct', 'Direct contact with participant'),
    ('indirect', 'Contact with person other than participant'),
    ('no_contact', 'No contact made'),
)

HOSPITALIZATION_REASONS = (
    (NOT_APPLICABLE, "Not applicable"),
    ('tb', 'Tuberculosis (TB, MTB)'),
    ('pneumonia', 'Pneumonia'),
    ('crypto_meningitis', 'Cryptococcal meningitis'),
    ('IRIS', 'Immune Reconstitution Inflammatory Syndrome (IRIS)'),
    ('OTHER_hiv_related', 'Other HIV-related illness'),
    ('pregnancy_related', 'Pregnancy-related care, including delivery'),
    ('injury_accident', 'Injury or accident'),
    ('chronic_disease',
     'Chronic disease related care, including high blood pressure, diabetes, '
     'cancer, mental illness (specify which)'),
    ('stroke', 'Stroke (or suspected stroke)'),
    ('medication_toxicity', 'Medication toxicity (specify)'),
    (OTHER, 'Other (specify)'),
    (DONT_KNOW, 'Don\'t know'),
)

REFERRAL_APPT_COMMENTS = (
    (NOT_APPLICABLE, "Not applicable"),
    ("conflict", "have another commitment"),
    ("prefer_other_facility",
     "prefer another health facility than the local clinic"),
    ("prefer_other_date", "prefer to come on my own convenient time"),
    ("undecided_thinking", "have to think about it"),
    ("undecided_accepting_status", "need time to accept my HIV status"),
    ("have_other_anc_appt",
     "have already registered with ANC and have another appointment"),
    ("personal_reasons", "personal reasons"),
)


VISIT_INFO_SOURCE = [
    ('subject', '1. Subject'),
    ('other_member', '2. Other household member'),
    (OTHER, '9. Other'),
]

VISIT_REASON = [
    ('consent', '1. Consent and Survey with subject'),
    ('absent', '2. Absentee'),
    ('undecided', '3. Undecided (with subject)'),
    ('refuse', '4. Refusal (with subject)'),
]


VISIT_UNSCHEDULED_REASON = (
    ('Routine oncology',
     _('Routine oncology clinic visit (i.e. planned chemo, follow-up)')),
    ('Ill oncology', _('Ill oncology clinic visit')),
    ('Patient called', _('Patient called to come for visit')),
    (OTHER, _('Other, specify:')),
)


RELATIONSHIP_TYPE = (
    ('Longterm partner', _('Longterm partner (>2 years) or spouse')),
    ('Boyfriend/Girlfriend', _('Boyfriend/Girlfriend')),
    ('Casual', _('Casual (known) partner')),
    ('One time partner', _('One time partner (previously unknown)')),
    ('Commercial sex worker', _('Commercial sex worker')),
    ('Other, specify', _('Other, specify')),
)


MAIN_PARTNER_RESIDENCY = (
    ('In this community', _('In this community')),
    ('On farm/cattle post', _('On farm/cattle post')),
    ('Outside this community', _('Outside this community')),
    (DWTA, _('Don\'t want to answer')),
)


SEX_REGULARITY = (
    ('All of the time', _('All of the time')),
    ('Sometimes', _('Sometimes')),
    ('Never', _('Never')),
)


INTERCOURSE_TYPE = (
    ('Vaginal', _('Vaginal sex')),
    ('Anal', _('Anal sex')),
    ('Both', _('Both vaginal and anal sex')),
)


#   CE001
MOBILITY = (
    ('no problems', _('I have no problems in walking about')),
    ('slight problems', _('I have slight problems in walking about')),
    ('moderate problems', _('I have moderate problems in walking about')),
    ('severe problems', _('I have severe problems in walking about')),
    ('unable to walk', _('I am unable to walk about')),
    (DWTA, _('Don\'t want to answer')),
)


SELF_CARE = (
    ('no problems', _('I have no problems washing or dressing myself')),
    ('slight problems',
     _('I have slight problems washing or dressing myself')),
    ('moderate problems',
     _('I have moderate problems washing or dressing myself')),
    ('severe problems',
     _('I have severe problems washing or dressing myself')),
    ('unable to wash', _('I am unable to wash or dress myself')),
    (DWTA, _('Don\'t want to answer')),
)


ACTIVITIES = (
    ('no problems', _('I have no problems doing my usual activities')),
    ('slight problems', _('I have slight problems doing my usual activities')),
    ('moderate problems',
     _('I have moderate problems doing my usual activities')),
    ('severe problems', _('I have severe problems doing my usual activities')),
    ('unable to', _('I am unable to do my usual activities')),
    (DWTA, _('Don\'t want to answer')),
)


PAIN = (
    ('no pain', _('I have no pain or discomfort')),
    ('slight pain', _('I have slight pain or discomfort')),
    ('moderate pain', _('I have moderate pain or discomfort')),
    ('severe pain', _('I have severe pain or discomfort')),
    ('extreme pain', _('I have extreme pain or discomfort')),
    (DWTA, _('Don\'t want to answer')),
)


ANXIETY = (
    ('not anxious', _('I am not anxious or depressed')),
    ('slightly anxious', _('I am slightly anxious or depressed')),
    ('moderately anxious', _('I am moderately anxious or depressed')),
    ('severely anxious', _('I am severely anxious or depressed')),
    ('extremely anxious', _('I am extremely anxious or depressed')),
    (DWTA, _('Don\'t want to answer')),
)


CARE_FACILITIES = (
    ('Government Clinic/Post', _('Government Primary Health Clinic/Post')),
    ('Chemist/Pharmacy', _('Chemist/Pharmacy')),
    ('Hospital Outpatient Department',
     _('Hospital Outpatient Department (including government and private)')),
    ('Private Doctor', _('Private Doctor')),
    ('Traditional or Faith Healer', _('Traditional or Faith Healer')),
    ('No visit in past 3 months', _('No visit in past 3 months')),
    (DWTA, _('Don\'t want to answer')),
)


CARE_REASON = (
    ('HIV-related care',
     _('HIV-related care, including TB and other opportunistic infections')),
    ('Pregnancy', _('Pregnancy-related care, including delivery')),
    ('Injuries', _('Injuries or accidents')),
    ('Chronic disease', _(
        'Chronic disease related care, including high blood pressure, '
        'diabetes, cancer, mental illness')),
    (OTHER, _('Other')),
    (DWTA, _('Don\'t want to answer')),
    (NONE, _('None')),
)


TRAVEL_HOURS = (
    (NONE, _('None')),
    ('Under 0.5 hour', _('Under 0.5 hour')),
    ('0.5 to under 1 hour', _('0.5 to under 1 hour')),
    ('1 to under 2 hours', _('1 to under 2 hours')),
    ('2 to under 3 hours', _('2 to under 3 hours')),
    ('More than 3 hours', _('More than 3 hours')),
    (DWTA, _('Don\'t want to answer')),
)


NO_MEDICALCARE_REASON = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('not thinking about HIV care',
     _('I am not thinking about HIV related medical/clinical '
       'care at this time')),
    ('I am not ready to start',
     _('HIV related medical/clinical care for my HIV infection '
       'is important to me but I am not ready to start it yet')),
    ('not yet tried to find a doctor',
     _('I have thought about starting HIV related medical/'
       'clinical care but have not yet tried to find a doctor or clinic')),
    ('not yet tried to make an appointment',
     _('I have found a doctor or clinic for HIV related '
       'medical/clinical care but have not yet tried to '
       'make an appointment')),
    ('no been successful yet',
     _('I have tried to obtain HIV related medical/clinical care from '
       'a doctor or clinic but have not been successful yet')),
    ('I have an appointment for HIV care',
     _('I have an appointment for HIV related medical/'
       'clinical care for my HIV infection but have not been for it yet')),
    ('don\'t know where to go',
     _('I don\'t know where to go for HIV related medical/clinical care')),
    ('I do not have the money',
     _('I do not have the money for HIV related medical/clinical care')),
    (DWTA, _('Don\'t want to answer')),
)


HEALTH_CARE_PLACE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('Government dispensary', _('Government dispensary')),
    ('Government health center', _('Government health center')),
    ('Government hospital', _('Government hospital')),
    ('Christian/mission health center', _('Christian/mission health center')),
    ('Islamic health center', _('Islamic health center')),
    ('Private health center for all illnesses',
     _('Private health center for all illnesses')),
    ('Private health center for HIV/AIDS',
     _('Private health center for HIV/AIDS')),
    ('Mobile services', _('Mobile services')),
    ('Plantation health center', _('Plantation health center')),
    ('NGO clinic', _('NGO clinic')),
    (DWTA, _('Don\'t want to answer')),
)


CARE_REGULARITY = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('0 times', _('0 times')),
    ('1 time', _('1 time')),
    ('2 times', _('2 times')),
    ('3 times', _('3 times')),
    ('4 times', _('4 times')),
    ('5 times', _('5 times')),
    ('6-10 times', _('6-10 times')),
    ('More than 10 times', _('More than 10 times')),
    (DWTA, _('Don\'t want to answer')),
)


DOCTOR_VISITS = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('always', _('All of the time (always)')),
    ('almost always', _('Most of the time (almost always)')),
    ('sometimes', _('Some of the time (sometimes)')),
    ('rarely', _('Almost none of the time (rarely)')),
    ('never', _('None of the time (never)')),
    (DWTA, _('Don\'t want to answer')),
)


JOB_TYPE = (
    ('piece job', _('Occassional or Casual employment (piece job)')),
    ('seasonal', _('Seasonal employment')),
    ('full-time', _('Formal wage employment (full-time)')),
    ('part-time', _('Formal wage employment (part-time)')),
    ('agric', _('Self-employed in agriculture')),
    ('self full-time', _('Self-employed making money, full time')),
    ('self part-time', _('Self-employed making money, part time')),
    (DWTA, _('Don\'t want to answer')),
    (OTHER, _('Other')),
)


OCCUPATION = (
    ('Farmer', _('Farmer (own land)')),
    ('Farm worker', _('Farm worker (work on employers land)')),
    ('Domestic Worker', _('Domestic Worker')),
    ('Tavern/Bar/Entertainment', _('Work at Tavern/Bar/Entertainment Venue')),
    ('Mining', _('Mining')),
    ('Tourism', _('Tourism/game parks')),
    ('Informal vendors', _('Informal vendors')),
    ('Commercial sex work', _('Commercial sex work')),
    ('Transport (e.g., trucker)', _('Transport (e.g., trucker)')),
    ('Factory worker', _('Factory worker')),
    ('Informal vendors', _('Informal vendors')),
    ('Clerical and office work', _('Clerical and office work')),
    ('Small business/shop work', _('Small business/shop work')),
    ('Professional', _('Professional')),
    ('Fishing', _('Fishing')),
    ('Uniformed services', _('Uniformed services')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

REASON_UNEMPLOYED = (
    ('waiting', _('Waiting to continue agricultural work')),
    ('unemployed- looking', _('Unemployed (looking for work)')),
    ('unemployed- waiting', _('Unemployed (waiting to start new work)')),
    ('unable to work', _('Unable to work (permanently sick or injured)')),
    ('student', _('Student/ Apprentice/ Volunteer')),
    ('housewife', _('Housewife/ Homemaker (not looking for work)')),
    ('retired', _('Retired')),
    (OTHER, _('Other')),
    ('not looking', _('Not looking for work')),
    (DWTA, _('Don\'t want to answer')),
)


EMPLOYMENT_INFO = (
    ('government sector', _('Yes, In the government sector')),
    ('private sector', _('Yes, in the private sector')),
    ('self-employed working on my own',
     _('Yes, self-employed working on my own')),
    ('self-employed with own employees',
     _('Yes, self-employed with own employees')),
    ('not working', _('No, not working')),
    (DWTA, _('Don\'t want to answer')),
)

JOB_DESCRIPTION = (
    ('farmer', _('Farmer (own land)')),
    ('farm work', _('Farm work on employers land')),
    ('domestic', _('Domestic worker')),
    ('bar/hotel', _('Work in bar/ hotel/ guest house/ entertainment venue')),
    ('fishing', _('Fishing')),
    ('mining', _('Mining')),
    ('tourism', _('Tourism/game parks')),
    ('shop', _('Working in shop / small business')),
    ('selling', _('Informal selling')),
    ('sexworker', _('Commercial sex work')),
    ('transport', _('Transport (trucker/ taxi driver)')),
    ('factory', _('Factory worker')),
    ('guard', _('Guard (security company)')),
    ('police', _('Police/ Soldier')),
    ('office', _('Clerical and office work')),
    ('govt worker', _('Government worker')),
    ('teacher', _('Teacher')),
    ('hcw', _('Health care worker')),
    ('other_professional', _('Other professional')),
    (DWTA, _('Don\'t want to answer')),
    (OTHER, _('Other')),
)

MONTHLY_INCOME = (
    ('None', _('No income')),
    ('1-199 pula', _('1-199 pula')),
    ('200-499 pula', _('200-499 pula')),
    ('500-999 pula', _('500-999 pula')),
    ('1000-4999 pula', _('1000-4999 pula')),
    ('5000-10,000 pula', _('5000-10,000 pula')),
    ('More than 10,000 pula', _('More than 10,000 pula')),
    (DWTA, _('Don\'t want to answer')),
)

SALARY = (
    ('Fixed salary', _('Fixed salary')),
    ('Paid daily', _('Paid daily')),
    ('Paid hourly', _('Paid hourly')),
    (DWTA, _('Don\'t want to answer')),
)

HOUSEHOLD_INCOME = (
    ('None', _('None')),
    ('1-200 pula', _('1-200 pula')),
    ('200-499 pula', _('200-499 pula')),
    ('500-999 pula', _('500-999 pula')),
    ('1000-4999 pula', _('1000-4999 pula')),
    ('5000-10,000 pula', _('5000-10,000 pula')),
    ('10,0000-20,000 pula', _('10,0000-20,000 pula')),
    ('More than 20,000 pula', _('More than 20,000 pula')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

OTHER_OCCUPATION = (
    ('None', _('None')),
    ('Studying', _('Studying')),
    ('Doing housework', _('Doing housework')),
    ('Looking for work', _('Looking for work')),
    ('Doing nothing (not looking for paid work)',
     _('Doing nothing (not looking for paid work)')),
    ('Retired/old age', _('Retired/old age')),
    ('Pregnant or recently pregnant', _('Pregnant or recently pregnant')),
    ('Sick or injured', _('Sick or injured')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)


HIV_DOC_TYPE = (
    ('Tebelopele', 'Tebelopele'),
    ('Lab result form', 'Lab result form'),
    ('ART Prescription', 'ART Prescription'),
    ('PMTCT Prescription', 'PMTCT Prescription'),
    ('Record of CD4 count', 'Record of CD4 count'),
    ('Ya Tsie Test Card', 'Ya Tsie Test Card'),
    (OTHER, 'Other OPD card or ANC card documentation'),
)

GRANT_TYPE = (
    ('Child support ', _('Child support ')),
    ('Old age pension', _('Old age pension')),
    ('Foster care', _('Foster care')),
    ('Disability', _('Disability (disability dependency)')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)


FLOORING_TYPE = (
    ('Dirt/earth', _('Dirt/earth ')),
    ('Wood, plank', _('Wood, plank')),
    ('Parquet/lino', _('Parquet/lino')),
    ('Cement', _('Cement')),
    ('Tile flooring', _('Tile flooring')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)


WATER_SOURCE = (
    ('Communal tap', _('Communal tap')),
    ('Standpipe/tap within plot', _('Standpipe/tap within plot')),
    ('Piped indoors', _('Piped indoors')),
    ('Borehore', _('Borehole')),
    ('Protected well', _('Protected well')),
    ('Unprotected/shallow well', _('Unprotected/shallow well')),
    ('River /dam/lake/pan', _('River /dam/lake/pan')),
    ('Bowser/tanker', _('Bowser/tanker')),
    (OTHER, _('Other, specify (including unknown):')),
    (DWTA, _('Don\'t want to answer')),
)


ENERGY_SOURCE = (
    ('Charcoal/wood', _('Charcoal/wood')),
    ('Paraffin', _('Paraffin')),
    ('Gas', _('Gas')),
    ('Electricity (mains)', _('Electricity (mains)')),
    ('Electricity (solar)', _('Electricity (solar)')),
    ('No cooking done', _('No cooking done')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)


TOILET_FACILITY = (
    ('Pit latrine within plot', _('Pit latrine within plot')),
    ('Flush toilet within plot', _('Flush toilet within plot')),
    ('Neighbour\'s flush toilet', _('Neighbour\'s flush toilet')),
    ('Neighbour\'s pit latrine', _('Neighbour''s pit latrine')),
    ('Communal flush toilet', _('Communal flush toilet')),
    ('Communal pit latrine', _('Communal pit latrine')),
    ('Pail bucket latrine', _('Pail bucket latrine')),
    ('Bush', _('Bush')),
    ('River or other body of water', _('River or other body of water')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)


SMALLER_MEALS = (
    ('Never', _('Never')),
    ('Rarely', _('Rarely')),
    ('Sometimes', _('Sometimes')),
    ('Often', _('Often')),
    (DWTA, _('Don\'t want to answer')),
)


ENROLMENT_REASON = (
    ('CD4 < 50', _('Most recent (within past 3 months) CD4 < 50')),
    ('CD4 50-100', _('Most recent (within past 3 months) CD4 50-100')),
    ('AIDS opportunistic infection/condition',
     _('Current AIDS opportunistic infection/condition')),
)


OPPORTUNISTIC_ILLNESSES = (
    ('Tuberculosis', _('Tuberculosis')),
    ('Wasting', _('Wasting')),
    ('Cryptococcosis', _('Cryptococcosis')),
    ('severe bacterial pneumonia', _('Recurrent severe bacterial pneumonia')),
    ('Esophageal candidiasis', _('Esophageal candidiasis')),
    ('Pneumocystis pneumonia', _('Pneumocystis pneumonia')),
    ('Kaposi\'s sarcoma', _('Kaposi\'s sarcoma')),
    ('Cervical cancer', _('Cervical cancer')),
    ('Non-Hodgkin\'s lymphoma', _('Non-Hodgkin\'s lymphoma')),
    ('Other, record', _('Other, record')),
    ('No current AIDS opportunistic illness',
     _('No current AIDS opportunistic illness')),
)


REFERRAL_REASONS = (
    ('receive', _('Referred to receive HIV result in clinic')),
    ('test', _('Referred to test in clinic')),
    ('protocol', _('Referred as per protocol')),
)

RELATION = (
    ('spouse', _('spouse')),
    ('parent', _('parent')),
    ('sibling', _('sibling')),
    ('child', _('child')),
    ('aunt/uncle', _('aunt/uncle')),
    ('cousin', _('cousin')),
    ('partner', _('partner/boyfriend/girlfriend')),
    (OTHER, _('Other, specify')),
)

WHEREACCESS_CHOICE = (
    ('Traditional, faith, or religious healer/doctor',
     _('Traditional, faith, or religious healer/doctor')),
    ('Pharmacy', _('Pharmacy')),
    ('Public or government',
     _('Public or government health facility or clinic')),
    ('Private health facility', _('Private health facility or clinic')),
    ('Community health worker', _('Community health worker')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

YES_NO_RECORD_REFUSAL = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
    ('record refusal', _('Participant does not want to provide record')),
)

YES_NO_UNSURE = (
    (YES, _(YES)),
    (NO, _(NO)),
    (NOT_SURE, _('Not Sure')),
)

STI_DX = (
    ('wasting', 'Severe weight loss (wasting) - more than 10% of body weight'),
    ('diarrhoea', 'Unexplained diarrhoea for one month'),
    ('yeast infection', 'Yeast infection of mouth or oesophagus'),
    ('pneumonia', 'Severe pneumonia or meningitis or sepsis'),
    ('PCP', 'PCP (Pneumocystis pneumonia)'),
    ('herpes', 'Herpes infection for more than one month'),
    (OTHER, 'Other'),
)

CHOICES_FROM_BCPPLIST = (
    ('Improved hygiene', _('Improved hygiene')),
    ('Reduced risk of HIV', _('Reduced risk of HIV')),
    ('Reduced risk of std',
     _('Reduced risk of other sexually transmitted diseases')),
    ('Reduced risk of cancer', _('Reduced risk of cancer')),
    ('heart_disease', _('Heart Disease or Stroke')),
    ('cancer', _('Cancer')),
    ('tb', _('Tuberculosis')),
    ('other_serious_infection', _('Other serious infection')),
    ('Radio', _('Radio')),
    ('TV', _('TV')),
    ('Landline telephone', _('Landline telephone')),
    ('Cell phone', _('Cell phone')),
    ('Computer', _('Computer')),
    ('Access to internet', _('Access to internet')),
    ('Refrigerator', _('Refrigerator')),
    ('Condoms, consistent use (male or female)',
     _('Condoms, consistent use (male or female)')),
    ('Injectable contraceptive', _('Injectable contraceptive')),
    ('Oral contraceptive', _('Oral contraceptive')),
    ('IUD', _('IUD')),
    ('Diaphragm or cervical cap', _('Diaphragm or cervical cap')),
    ('hythm or menstrual cycle timing', _('Rhythm or menstrual cycle timing')),
    ('Withdrawal', _('Withdrawal')),
    ('Myocardial infarction (heart attack)',
     _('Myocardial infarction (heart attack)')),
    ('Congestive cardiac failure', _('Congestive cardiac failure')),
    ('Stroke (cerebrovascular accident, CVA)',
     _('Stroke (cerebrovascular accident, CVA)')),
    ('Partner or spouse', _('Partner or spouse')),
    ('Siblings', _('Siblings')),
    (ALONE, _('Alone')),
    ('Extended family', _('Extended family')),
    ('Traditional, faith, or religious healer/doctor',
     _('Traditional, faith, or religious healer/doctor')),
    ('Pharmacy', _('Pharmacy')),
    ('ublic or government health facility or clinic',
     _('Public or government health facility or clinic')),
    ('Private health facility or clinic',
     _('Private health facility or clinic')),
    ('Community health worker', _('Community health worker')),
    ('Water', _('Water')),
    ('Sewer (sanitation)', _('Sewer (sanitation)')),
    ('Housing', _('Housing')),
    ('Roads', _('Roads')),
    ('Malaria', _('Malaria')),
    ('HIV/AIDS', _('HIV/AIDS')),
    ('Schools', _('Schools')),
    ('Unemployment', _('Unemployment')),
    ('In this community', _('In this community')),
    ('Outside community', _('Outside community')),
    ('Farm within', _('Farm within this community')),
    ('Farm outside this community', _('Farm outside this community')),
    ('cattlepost within', _('Cattle post within this community')),
    ('cattlepost outside', _('Cattle post outside this community')),
    ('Motor vehicle (car,truck,taxi, etc)',
     _('Motor vehicle (car,truck,taxi, etc)')),
    ('Tractor', _('Tractor')),
    ('Bicycle', _('Bicycle')),
    ('Motorcycle/scooter', _('Motorcycle/scooter')),
    ('Donkey or cow cart', _('Donkey or cow cart')),
    ('Donkey/horses', _('Donkey/horses')),
)

COUNSELING_SITE = (
    ('IN_HOME', 'In home'),
    ('MOBILE', 'Mobile Unit'),
    ('TENT', 'Tent'),
    ('CLINIC', 'Clinic'),
)

PLACE_CIRC = (
    ('Government clinic or hospital', _('Government clinic or hospital')),
    ('Traditional location (Bogerwa)', _('Traditional location (Bogerwa)')),
    ('Outreach site (mobile or temporary center)',
     _('Outreach site (mobile or temporary center)')),
    ('Private practitioner', _('Private practitioner')),
    (NOT_SURE, _('I am not sure')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

WHYCIRC_CHOICE = (
    ('Prevent HIV/AIDS', _('Prevent HIV/AIDS')),
    ('Other medical reason', _('Other medical reason')),
    ('Personal preference', _('Personal preference')),
    ('Improved hygiene', _('Improved hygiene')),
    ('Cultural tradition and/or religion',
     _('Cultural tradition and/or religion')),
    ('Acceptance by sexual partner(s)', _('Acceptance by sexual partner(s)')),
    ('Acceptance by family, friends, and/or community',
     _('Acceptance by family, friends, and/or community')),
    (NOT_SURE, _('I am not sure')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

WHERECIRC_CHOICE = (
    (YES, _('Yes')),
    ('No, not sexually active and will not become sexual '
     'active', _('No, not sexually active and will not become sexual active')),
    ('No, prior surgical sterilization',
     _('No, prior surgical sterilization')),
    ('No, partner(s) surgically sterilized',
     _('No, partner(s) surgically sterilized')),
    ('No, post-menopause',
     _('No, post-menopause (at least 24 consecutive months without a period)')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

TIME_UNIT_CHOICE = (
    ('Days', _('Days')),
    ('Months', _('Months')),
    ('Years', _('Years')),
    (DWTA, _('Don\'t want to answer')),
)

DXCANCER_CHOICE = (
    ('Kaposi\'s sarcoma (KS)', 'Kaposi\'s sarcoma (KS)'),
    ('Cervical cancer', 'Cervical cancer'),
    ('Breast cancer', 'Breast cancer'),
    ('Non-Hodgkin\'s lymphoma (NHL)', 'Non-Hodgkin\'s lymphoma (NHL)'),
    ('Colorectal cancer', 'Colorectal cancer'),
    ('Prostate cancer', 'Prostate cancer'),
    ('Cancer of mouth, throat, voice box (larynx)',
     'Cancer of mouth, throat, voice box (larynx)'),
    ('Cancer of oesophagus', 'Cancer of oesophagus'),
    (OTHER, 'Other, specify:'),
    (DWTA, 'Don\'t want to answer'),
)

COMMUNITIES = (
    ('Bokaa', _('Bokaa')),
    ('Digawana', _('Digawana')),
    ('Gumare', _('Gumare')),
    ('Gweta', _('Gweta')),
    ('Lentsweletau', _('Lentsweletau')),
    ('Lerala', _('Lerala')),
    ('Letlhakeng', _('Letlhakeng')),
    ('Mmandunyane', _('Mmandunyane')),
    ('Mmankgodi', _('Mmankgodi')),
    ('Mmadinare', _('Mmadinare')),
    ('Mmathethe', _('Mmathethe')),
    ('Masunga', _('Masunga')),
    ('Maunatlala', _('Maunatlala')),
    ('Mathangwane', _('Mathangwane')),
    ('Metsimotlhabe', _('Metsimotlhabe')),
    ('Molapowabojang', _('Molapowabojang')),
    ('Nata', _('Nata')),
    ('Nkange', _('Nkange')),
    ('Oodi', _('Oodi')),
    ('Otse', _('Otse')),
    ('Rakops', _('Rakops')),
    ('Ramokgonami', _('Ramokgonami')),
    ('Ranaka', _('Ranaka')),
    ('Sebina', _('Sebina')),
    ('Sefhare', _('Sefhare')),
    ('Sefophe', _('Sefophe')),
    ('Shakawe', _('Shakawe')),
    ('Shoshong', _('Shoshong')),
    ('Tati_Siding', _('Tati_Siding')),
    ('Tsetsebjwe', _('Tsetsebjwe')),
    (OTHER, _('Other non study community')),
)

COMMUNITY_NA = tuple(
    [(NOT_APPLICABLE, _('Not Applicable'))] + list(COMMUNITIES))

VERBAL_HIVRESULT_CHOICE = (
    (POS, _('HIV Positive')),
    (NEG, _('HIV Negative')),
    (IND, _('Indeterminate')),
    (UNK, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)


COMMUNITY_ENGAGEMENT_CHOICE = (
    ('Very active', _('Very active')),
    ('Somewhat active', _('Somewhat active')),
    ('Not active at all', _('Not active at all')),
    (DWTA, _('Don\'t want to answer')),
)


VOTE_ENGAGEMENT_CHOICE = (
    (YES, _('Yes')),
    (NO, _('No')),
    (NOT_APPLICABLE, _('Not applicable (no election, can\'t vote)')),
    (DWTA, _('Don\'t want to answer')),
)


SOLVE_ENGAGEMENT_CHOICE = (
    (YES, _('Yes')),
    (NO, _('No')),
    (DONT_KNOW, _('Don\'t know')),
    (DWTA, _('Don\'t want to answer')),
)

MARITAL_STATUS_CHOICE = (
    ('Single/never married', _('Single/never married')),
    ('Married', _('Married (common law/civil or customary/traditional)')),
    ('Divorced/separated', _('Divorced or formally separated')),
    ('Widowed', _('Widowed')),
    (DWTA, _('Don\'t want to answer')),
)

REASON_CIRC_CHOICE = (
    ('Circumcision never offered to me',
     _('Circumcision never offered to me')),
    ('Procedure might be painful', _('Procedure might be painful')),
    ('Did not know where to go for circumcision',
     _('Did not know where to go for circumcision')),
    ('Did not have the time or money for circumcision',
     _('Did not have the time or money for circumcision')),
    ('I might not be able to work or be active',
     _('I might not be able to work or be active')),
    ('My partner might not approve', _('My partner might not approve')),
    ('My family/friends might not approve',
     _('My family/friends might not approve')),
    ('There might be a medical complication',
     _('There might be a medical complication')),
    ('The healing time is very long', _('The healing time is very long')),
    ('It will be hard to not have sex or masturbate for 6 weeks',
     _('It will be hard to not have sex or masturbate '
       'for 6 weeks')),
    ('Sex might not feel the same', _('Sex might not feel the same')),
    ('I may not like the way my penis looks',
     _('I may not like the way my penis looks')),
    ('I may not like the way my penis feels',
     _('I may not like the way my penis feels')),
    ('I could die from the procedure', _('I could die from the procedure')),
    (OTHER, _('Other, specify:')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

FUTURE_REASONS_SMC_CHOICE = (
    ('More information about benefits', _('More information about benefits')),
    ('More information about risks', _('More information about risks')),
    ('If there was no or minimal pain with circumcision',
     _('If there was no or minimal pain with circumcision')),
    ('If circumcision could be done close to my home',
     _('If circumcision could be done close to my home')),
    ('If the kgosi recommended circumcision for all men',
     _('If the kgosi recommended circumcision for all men')),
    ('If I received time off work to recover from circumcision',
     _('If I received time off work to recover from '
       'circumcision')),
    ('If my sexual partner encouraged me',
     _('If my sexual partner encouraged me')),
    ('If one or both of my parents encouraged me',
     _('If one or both of my parents encouraged me')),
    ('If my friends encouraged me', _('If my friends encouraged me')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

AWARE_FREE_CHOICE = (
    (NOT_APPLICABLE, _('Not applicable')),
    ('Radio', _('Radio')),
    ('Television', _('Television')),
    ('Friend told me', _('Friend told me')),
    ('Family told me', _('Family told me')),
    ('Health worker told me', _('Health worker told me')),
    ('Ya Tsie staff told me', _('Ya Tsie staff told me')),
    ('Kgosi told us', _('Kgosi told us')),
    ('I heard it at the kgotla', _('I heard it at the kgotla')),
    ('I read a brochure delivered to my home',
     _('I read a brochure delivered to my home')),
    ('I read it in the newspaper', _('I read it in the newspaper')),
    ('Heard it at a community event', _('Heard it at a community event')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

DX_TB_CHOICE = (
    ('Pulmonary tuberculosis', 'Pulmonary tuberculosis'),
    ('Extrapulmonary (outside the lungs) tuberculosis',
     'Extrapulmonary (outside the lungs) tuberculosis'),
    (OTHER, 'Other, specify:'),
    (DWTA, 'Don\'t want to answer'),
)

ALCOHOL_CHOICE = (
    ('Never', _('Never')),
    ('Less then once a week', _('Less then once a week')),
    ('Once a week', _('Once a week')),
    ('2 to 3 times a week', _('2 to 3 times a week')),
    ('more than 3 times a week', _('more than 3 times a week')),
    (DWTA, _('Don\'t want to answer')),
)

EDUCATION_CHOICE = (
    ('Non formal', _('Non formal')),
    ('Primary', _('Primary')),
    ('Junior Secondary', _('Junior Secondary')),
    ('Senior Secondary', _('Senior Secondary')),
    ('Higher than senior secondary (university, diploma, '
     'etc.)', _('Higher than senior secondary (university, diploma, etc.)')),
    (DWTA, _('Don\'t want to answer')),
)

WHY_NO_ARV_CHOICE = (
    (NOT_APPLICABLE, _('Not applicable')),
    ('Did not feel sick', _('Did not feel sick')),
    ('Was afraid treatment would make me feel bad/sick',
     _('Was afraid treatment  would make me feel bad/sick')),
    ('Difficulty finding someone to go with me for counseling (mopati)',
     _('Difficulty finding someone to go with '
       'me for counseling (mopati)')),
    ('Hard due to work responsibilities',
     _('Hard due to work responsibilities')),
    ('Hard due to family/childcare responsibilities',
     _('Hard due to family/childcare responsibilities')),
    ('Transportation costs', _('Transportation costs')),
    ('Was afraid of someone (friends/family) seeing me at the HIV clinic',
     _('Was afraid of someone (friends/family)'
       ' seeing me at the HIV clinic')),
    ('Sexual partner advised against taking',
     _('Sexual partner advised against taking')),
    ('Family or friends advised against taking',
     _('Family or friends advised against taking')),
    ('Traditional healer advised against taking',
     _('Traditional healer advised against taking')),
    ('Religious beliefs', _('Religious beliefs')),
    ('Cultural beliefs', _('Cultural beliefs')),
    ('High CD4', _('High CD4')),
    ('Cost', _('Cost')),
    (OTHER, _('Other, specify:')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

WHY_ARV_STOP_CHOICE = (
    (NOT_APPLICABLE, _('Not applicable')),
    ('Did not feel they were helping', _('Did not feel they were helping')),
    ('ARVs made me feel bad or sick', _('ARVs made me feel bad or sick')),
    ('Difficulty finding someone to go with me for counseling '
     '(mopati)',
     _('Difficulty finding someone to go with me for counseling (mopati)')),
    ('Hard due to work responsibilities',
     _('Hard due to work responsibilities')),
    ('Hard due to family/childcare responsibilities',
     _('Hard due to family/childcare responsibilities')),
    ('Doctor or nurse at clinic told me to stop',
     _('Doctor or nurse at clinic told me to stop')),
    ('Transportation costs', _('Transportation costs')),
    ('Cost/could not afford', _('Cost/could not afford')),
    ('Was afraid of someone (friends/family) seeing me at the HIV'
     ' clinic',
     _('Was afraid of someone (friends/family) seeing me at the HIV clinic')),
    ('Sexual partner advised against taking',
     _('Sexual partner advised against taking')),
    ('Family or friends advised against taking',
     _('Family or friends advised against taking')),
    ('Traditional healer advised against taking',
     _('Traditional healer advised against taking')),
    ('Religious beliefs', _('Religious beliefs')),
    ('Cultural beliefs', _('Cultural beliefs')),
    (OTHER, _('Other, specify:')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

ADHERENCE_4DAY_CHOICE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('Zero', _('Zero days')),
    ('One day', _('One day')),
    ('Two days', _('Two days')),
    ('Three days', _('Three days')),
    ('Four days', _('Four days')),
    (DWTA, _('Don\'t want to answer')),
)

ADHERENCE_4WK_CHOICE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('Very poor', _('Very poor')),
    ('Poor', _('Poor')),
    ('Fair', _('Fair')),
    ('Good', _('Good')),
    ('Very good', _('Very good')),
    (DWTA, _('Don\'t want to answer')),
)

NO_MEDICAL_CARE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('Did not feel sick', _('Did not feel sick')),
    ('Did not know I should get HIV care',
     _('Did not know I should get HIV care')),
    ('Did not have time due to work responsibilities',
     _('Did not have time due to work responsibilities')),
    ('Did not have time due to family/childcare responsibilities',
     _('Did not have time due to family/childcare '
       'responsibilities')),
    ('Transportation costs', _('Transportation costs')),
    ('Was afraid of someone (friends/family) seeing me at the HIV clinic',
     _('Was afraid of someone (friends/family) '
       'seeing me at the HIV clinic')),
    ('Traditional healer advised against going',
     _('Traditional healer advised against going')),
    ('Religious beliefs', _('Religious beliefs')),
    ('Cultural beliefs', _('Cultural beliefs')),
    ('Not provided free of charge for non-citizens',
     _('Not provided free of charge for non-citizens')),
    (OTHER, _('Other, specify:')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

LOWEST_CD4_CHOICE = (
    ('0-49', _('0-49')),
    ('50-99', _('50-99')),
    ('100-199', _('100-199')),
    ('200-349', _('200-349')),
    ('350-499', _('350-499')),
    ('500 or more', _('500 or more')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

WHY_NO_HIV_TESTING_CHOICE = (
    ('I already knew I am HIV positive',
     _('I already knew I am HIV positive')),
    ('I recently tested', _('I recently tested (I know my status)')),
    ('I didn\'t believe I was at risk of getting HIV',
     _('I didn\'t believe I was at risk of getting HIV')),

    ('I am afraid to find out the result',
     _('I am afraid to find out the result')),
    ('I am afraid of what others would think of me',
     _('I am afraid of what others would think of me')),
    ('Family/friends did not want me to get an HIV test',
     _('Family/friends did not want me to get an HIV test')),
    ('I didn\'t have time due to work', _('I didn\'t have time due to work')),
    ('I didn\'t have time due to family obligations',
     _('I didn\'t have time due to family obligations')),
    ('My sexual partner did not want me to get an HIV test',
     _('My sexual partner did not want me to get an HIV test')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

WHEN_HIV_TEST_CHOICE = (
    ('In the last month', _('In the last month')),
    ('1 to 5 months ago', _('1 to 5 months ago')),
    ('6 to 12 months ago', _('6 to 12 months ago')),
    ('more than 12 months ago', _('more than 12 months ago')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

VERBAL_HIV_RESULT_CHOICE = (
    (POS, _('HIV Positive')),
    (NEG, _('HIV Negative')),
    (IND, _('Indeterminate')),
    (UNK, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

WHERE_HIV_TEST_CHOICE = (
    ('Tebelopele VCT center', _('Tebelopele VCT center')),
    ('Antenatal care at healthcare facility',
     _('Antenatal care at healthcare facility (including private clinics)')),
    ('Other (not antenatal care) at healthcare facility',
     _('Other (not antenatal care) at healthcare '
       'facility (including private clinics)')),
    ('In my house as part of door-to-door services',
     _('In my house as part of door-to-door services')),
    ('In a mobile tent or vehicle in my neighborhood',
     _('In a mobile tent or vehicle in my neighborhood')),
    ('Ya_Tsie HIV Test Campaign', _('Ya Tsie HIV Test Campaign')),
    (OTHER, _('Other, specify:')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

WHY_HIV_TEST_CHOICE = (
    ('I was worried I might have HIV and wanted to know my '
     'status', _('I was worried I might have HIV and wanted to know my status')),
    ('I heard from someone I trust that it is important for me to get tested for '
     'HIV ', _('I heard from someone I trust that it is important '
               'for me to get tested for HIV ')),
    ('I was at a health facility where the doctor/nurse recommended '
     'I get tested for HIV during '
     'the same visit', _('I was at a health facility where the doctor/nurse'
                         ' recommended I get '
                         'tested for HIV during the same visit')),
    ('I read information on a brochure/flier that it is important for '
     'me to get tested for '
     'HIV', _('I read information on a brochure/flier that it is '
              'important for me to get tested for HIV')),
    ('from_ya_tsie', _('I had information from the Ya Tsie study '
                       'that it was important to get tested for HIV')),
    (OTHER, _('Other')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

HIV_RESULT = (
    (POS, 'HIV Positive (Reactive)'),
    (NEG, 'HIV Negative (Non-reactive)'),
    (IND, 'Indeterminate'),
    (DECLINED, 'Participant declined testing'),
    (NOT_PERFORMED,
     'Test could not be performed (e.g. supply outage, technical problem)'),
)

QUANTIFIER = (
    ('greater_than', _('Greater Than')),
    ('equal_to', _('Equal To')),
    ('less_than', _('Less Than')),
    (OTHER, _('Other, specify:')),
)

EASY_OF_USE = (
    ('easy', _('Easy')),
    ('Very easy', _('Very Easy')),
    ('Fairly easy', _('Fairly easy')),
    ('Difficult', _('Difficult')),
    ('Very difficult', _('Very difficult')),
)

SEXDAYS_CHOICE = (
    (DAYS, _('Days')),
    (MONTHS, _('Months')),
    (DWTA, _('Don\'t want to answer')),
)


LASTSEX_CHOICE = (
    (DAYS, _('Days')),
    (MONTHS, _('Months')),
    (YEARS, _('Years')),
    (DWTA, _('Don\'t want to answer')),
)

FIRSTRELATIONSHIP_CHOICE = (
    ('Long-term partner', _('Long-term partner (>2 years) or spouse')),
    ('2 years or spouse', _('2 years or spouse')),
    ('Boyfriend/Girlfriend', _('Boyfriend/Girlfriend')),
    ('Casual (known) partner', _('Casual (known) partner')),
    ('One time partner (previously unknown)',
     _('One time partner (previously unknown)')),
    ('Commercial sex worker', _('Commercial sex worker')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

FIRST_PARTNER_HIV_CHOICE = (
    (POS, _('HIV positive')),
    (NEG, _('HIV negative')),
    (NOT_SURE, _('I am not sure HIV status')),
    (DWTA, _('Don\'t want to answer')),
)


FIRST_DISCLOSE_CHOICE = (
    (YES, _('Yes')),
    (NO, _('No')),
    ('Did not know my HIV status', _('Did not know my HIV status')),
    (DWTA, _('Don\'t want to answer')),
)

FIRST_CONDOM_FREQ_CHOICE = (
    ('All of the time', _('All of the time')),
    ('Sometimes', _('Sometimes')),
    ('Never', _('Never')),
    (DWTA, _('Don\'t want to answer')),
)

FREQ_IN_YEAR = (
    ('Less than once a month', _('Less than once a month')),
    ('About once a month', _('About once a month')),
    ('2-3 times a month', _('2-3 times a month')),
    ('About once a week', _('About once a week')),
    ('2 or more times a week', _('2 or more times a week'))
)

AGE_RANGES = (
    ('less or equal to 18 years old', _('less or equal to 18 years old')),
    ('19-29', _('19-29 years old')),
    ('30-39', _('30-39 years old')),
    ('40-49', _('40-49 years old')),
    ('50-59', _('50-59 years old')),
    ('60 or older', _('60 year or older')),
    (NOT_SURE, _('Not sure')),
    (DWTA, 'Don\'t want to answer'),
)

PREG_ARV_CHOICE = (
    ('Yes, AZT (single drug, twice a day)',
     _('Yes, AZT (single drug, twice a day)')),
    ('Yes, HAART ', _(
        'Yes, HAART [multiple drugs like Atripla, Truvada, '
        'or Combivir taken once or twice a day]')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
    (NO, _('No ARV\'s')),
)

PARTIAL_PARTICIPATION_TYPE = (
    (NOT_APPLICABLE, _('Not Applicable')),
    ('Changed mind midway', _('Participant changed mind')),
)

ANC_REG_CHOICE = (
    (YES, _('Yes')),
    ('No, but I will go for antenatal care',
     _('No, but I will go for antenatal care')),
    ('No and I am not planning on going for antenatal care',
     _('No and I am not planning on going for antenatal care')),
    (DWTA, _('Don\'t want to answer')),
)

MARITAL_STATUS_CHOICE = (
    ('Single/never married', _('Single/never married')),
    (MARRIED, _('Married (common law/civil or customary/traditional)')),
    ('Divorced/separated', _('Divorced or formally separated')),
    ('Widowed', _('Widowed')),
    (DWTA, _('Don\'t want to answer')),
)

LENGTH_RESIDENCE_CHOICE = (
    ('Less than 6 months', _('Less than 6 months')),
    ('6 months to 12 months', _('6 months to 12 months')),
    ('1 to 5 years', _('1 to 5 years')),
    ('More than 5 years', _('More than 5 years')),
    (DWTA, _('Don\'t want to answer')),
)

NIGHTS_AWAY_CHOICE = (
    (ZERO, _('Zero nights')),
    ('1-6 nights', _('1-6 nights')),
    ('1-2 weeks', _('1-2 weeks')),
    ('3 weeks to less than 1 month', _('3 weeks to less than 1 month')),
    ('1-3 months', _('1-3 months')),
    ('4-6 months', _('4-6 months')),
    ('more than 6 months', _('more than 6 months')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

CATTLEPOST_LANDS_CHOICE = (
    (NOT_APPLICABLE, _('Not Applicable')),
    ('Farm/lands', _('Farm/lands')),
    ('Cattle post', _('Cattle post')),
    ('Other community', _('Other community, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

ALCOHOL_SEX = (
    (NOT_APPLICABLE, _('Not Applicable')),
    ('Neither of us', _('Neither of us')),
    ('My partner', _('My partner')),
    ('Myself', _('Myself')),
    ('Both of us', _('Both of us')),
    (DWTA, _('Don\'t want to answer')),
)

FIRST_PARTNER_HIV_CHOICE = (
    (POS, _('HIV-positive')),
    (NEG, _('HIV-negative')),
    (NOT_SURE, _('I am not sure HIV status')),
    (DWTA, _('Don\'t want to answer')),
)

# FIXME: responses are not unique
KEPT_APPT = (
    (YES, 'Yes, kept appointment'),
    ('attended_other_date',
     'No but attended a visit at the HIV care clinic to which '
     'they were referred on another date'),
    ('attended_different_clinic',
     'No but attended a visit at a different HIV clinic'),
    ('went_different_clinic', 'I went to a different clinic'),
    ('failed_attempt',
     'No but tried to attend an HIV care clinic and left before '
     'I saw a healthcare provider'),
    ('didnt_attend', 'I have not been to any HIV care clinic')
)

PARTNER_AGE = (
    ('lte_18', 'less or equal to 18 years old'),
    ('gte_19', '19 years old or older'),
    (DONT_KNOW, 'Not sure'),
    (DWTA, _('Don\'t want to answer')),
    (NOT_APPLICABLE, "Not applicable"),

)

TYPE_OF_EVIDENCE = (
    ("self_report", "Self-Report Only"),
    ("opr_card", "OPD Card"),
    ("clinic_paperwork", "Clinic paperwork"),
    (OTHER, "Other ")
)

REASON_RECOMMENDED = (
    ("low_cd4", "Low CD4"),
    ("high_viral_load", "High viral load"),
    ("pregnancy_breastfeeding", "Pregnancy or breastfeeding"),
    ("tuberculosis", "Tuberculosis"),
    ("cancer", "Cancer"),
    (OTHER, "Other, specify"),
    (DONT_KNOW, "Do not know"),
)

HEALTH_CARE_FACILITY = (
    ("clinic", "Clinic"),
    ("primary_hospital", "Primary Hospital"),
    ("district_hospital", "District Hospital"),
    ("tertiary_hospital", "Tertiary Hospital"),
    ("private_doctor", "Private Doctor/Hospital"),
    (NOT_APPLICABLE, "Not applicable"),
)

# TOBACCO_SMOKING = (
#     ("never", "Never"),
#     ("ever", "Ever"),
#     ("prior", "Prior"),
#     ("current", "Current"),
#     (NOT_APPLICABLE, "Not applicable")
# )

PANEL_CHOICE = (
    ('ELISA', _('ELISA')),
    ('Microtube', _('Microtube')),
    ('Research Blood Draw', _('Research Blood Draw')),
    ('Viral Load', _('Viral Load')),
    ('Venous (HIV)', _('Venous (HIV)')),
)

YES_NO_REGIMEN = (
    (YES, 'Yes, this is the first regimen'),
    (NO, 'No, I previously took at least 1 different ARV (and was switched '
         'to this regimen)')
)

WEEKS_MONTHS = (
    ('Weeks', 'weeks'),
    ('Months', 'months')
)

HOSPITALIZED_EVIDENCE = (
    ('Self-report', 'Self report'),
    ('Medical-card', 'Medical Card'),
    ('Both', 'Both'),
    (OTHER, 'Other reason, specify')
)

COUNTRIES = (
    ('Algeria', 'Algeria'),
    ('Angola', 'Angola'),
    ('Botswana', 'Botswana'),
    ('Brazil', 'Brazil'),
    ('Cameroon', 'Cameroon'),
    ('Canada', 'Canada'),
    ('China', 'China'),
    ('Kenya', 'Kenya'),
    ('Lesotho', 'Lesotho'),
    ('Mauritius', 'Mauritius'),
    ('Mozambique', 'Mozambique'),
    ('Nigeria', 'Nigeria'),
    ('South Africa', 'South Africa'),
    ('Swaziland', 'Swaziland'),
    ('Tanzania', 'Tanzania'),
    ('United States', 'United States'),
    ('Zambia', 'Zambia'),
    ('Zimbabwe', 'Zimbabwe'),
    (OTHER, 'OTHER'),
)

RELIGION = (
    ('anglican', 'Anglican'),
    ('apostolic', 'Apostolic'),
    ('baptist', 'Baptist'),
    ('catholic', 'Catholic'),
    ('evangelical', 'Evangelical'),
    ('methodist', 'Methodist'),
    ('pentecostal', 'Pentecostal'),
    ('traditionalist', 'Traditionalist'),
    ('zcc', 'ZCC'),
    ('muslim', 'Islam'),
    ('hindu', 'Hinduism'),
    ('buddhist', 'Buddhism'),
    (OTHER, 'Other, specify'),
    ('No affiliation', 'No affiliation'),
)


ETHNIC_GROUP = (
    ('Babirwa', 'Babirwa'),
    ('Bahambukushu', 'Bahambukushu'),
    ('Baherero', 'Baherero'),
    ('Bahurutshe', 'Bahurutshe'),
    ('Bakalaka', 'Bakalaka'),
    ('Bakgatla', 'Bakgatla'),
    ('Bakwena', 'Bakwena'),
    ('Balete', 'Balete'),
    ('Bangwaketse', 'Bangwaketse'),
    ('Bangwato', 'Bangwato'),
    ('Bakgalagadi', 'Bakgalagadi'),
    ('Bakhurutse', 'Bakhurutse'),
    ('Barolong', 'Barolong'),
    ('Basarwa', 'Basarwa'),
    ('Basobea', 'Basobea'),
    ('Batalaote', 'Batalaote'),
    ('Batawana', 'Batawana'),
    ('Batlokwa', 'Batlokwa'),
    ('Batswapong', 'Batswapong'),
    ('Bayei', 'Bayei'),
    ('Bazezuri/Shona', 'Bazezuri'),
    ('Indian African', 'Indian African'),
    ('Asian', 'Asian'),
    ('White African', 'White African'),
    (OTHER, 'Other, specify'),
    (DWTA, 'Don\'t want to answer'),
)

REFERRAL_LETTER_YES_NO_REFUSED = (
    (YES, 'Yes, subject has been handed a referral letter'),
    (NO, 'No, subject has not been handed a referral letter'),
    (REFUSED, 'Subject refused referral the referral letter'))

PIMA = (
    ('Participant Declined', 'Participant Declined'),
    ('Multiple PIMA malfunction', 'Multiple PIMA malfunction'),
    ('Failed Blood Collection', 'Failed Blood Collection'),
    (OTHER, _('Other, specify:')),
)


ENROLLMENT_SITES = (
    ('gaborone_private_hospital', ' Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_Hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)


VERBALHIVRESULT_CHOICE = (
    (POS, _('HIV Positive')),
    (NEG, _('HIV Negative')),
    (IND, _('Indeterminate')),
    (UNK, _('I am not sure')),
    ('not_answering', _('Don\'t want to answer')),
)

INABILITY_TO_PARTICIPATE_REASON = (
    (ABLE_TO_PARTICIPATE, ('ABLE to participate')),
    (MENTAL_INCAPACITY, ('Mental Incapacity')),
    ('Deaf/Mute', ('Deaf/Mute')),
    ('Too sick', ('Too sick')),
    ('Incarcerated', ('Incarcerated')),
    (OTHER, ('Other, specify.')),
    (NOT_APPLICABLE, ('Not applicable')),
)
