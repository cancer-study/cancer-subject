from django.utils.translation import ugettext_lazy as _
from edc_constants.constants import DONT_KNOW, NONE, NOT_SURE, DECLINED
from edc_constants.constants import NEG, IND, UNK, OTHER
from edc_constants.constants import YES, NO, DWTA, NOT_APPLICABLE, POS

from cancer_subject.constants import (ABLE_TO_PARTICIPATE, MENTAL_INCAPACITY,
                                      REFUSED, ALONE, NOT_PERFORMED, DAYS, MONTHS,
                                      YEARS, MARRIED, ZERO)


ACTIVITIES = (
    ('no_problems', _('I have no problems doing my usual activities')),
    ('slight_problems', _('I have slight problems doing my usual activities')),
    ('moderate_problems',
     _('I have moderate problems doing my usual activities')),
    ('severe_problems', _('I have severe problems doing my usual activities')),
    ('unable_to', _('I am unable to do my usual activities')),
    (DWTA, _('Don\'t want to answer')),
)

AGREE_STRONGLY = (
    ('strongly_disagree', _('Strongly disagree')),
    ('disagree', _('Disagree')),
    ('uncertain', _('Uncertain')),
    ('agree', _('Agree')),
    ('strongly_agree', _('Strongly agree')),
    (DWTA, _('Don\'t want to answer')),
)

ANXIETY = (
    ('not_anxious', _('I am not anxious or depressed')),
    ('slightly_anxious', _('I am slightly anxious or depressed')),
    ('moderately_anxious', _('I am moderately anxious or depressed')),
    ('severely_anxious', _('I am severely anxious or depressed')),
    ('extremely_anxious', _('I am extremely anxious or depressed')),
    (DWTA, _('Don\'t want to answer')),
)

APPT_GRADING = (
    ('firm', 'Firm appointment'),
    ('weak', 'Possible appointment'),
    ('guess', 'Estimated by RA'),
)

APPT_LOCATIONS = (
    ('home', 'At home'),
    ('work', 'At work'),
    ('clinic', 'At clinic'),
    (OTHER, 'Other location'),
)

CARE_FACILITIES = (
    ('govt_clinic_or_post', _('Government Primary Health Clinic/Post')),
    ('chemist_or_pharmacy', _('Chemist/Pharmacy')),
    ('hospital_outpatient_department',
     _('Hospital Outpatient Department (including government and private)')),
    ('private_doctor', _('Private Doctor')),
    ('traditional_or_faith_healer', _('Traditional or Faith Healer')),
    ('no_visit', _('No visit in past 3 months')),
    (DWTA, _('Don\'t want to answer')),
)

CARE_REASON = (
    ('HIV_related_care',
     _('HIV-related care, including TB and other opportunistic infections')),
    ('pregnancy', _('Pregnancy-related care, including delivery')),
    ('injuries', _('Injuries or accidents')),
    ('chronic_disease', _(
        'Chronic disease related care, including high blood pressure, '
        'diabetes, cancer, mental illness')),
    (OTHER, _('Other')),
    (DWTA, _('Don\'t want to answer')),
    (NONE, _('None')),
)

CARE_REGULARITY = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('0_times', _('0 times')),
    ('1_time', _('1 time')),
    ('2_times', _('2 times')),
    ('3_times', _('3 times')),
    ('4_times', _('4 times')),
    ('5_times', _('5 times')),
    ('6_to_10_times', _('6-10 times')),
    ('more_than_10_times', _('More than 10 times')),
    (DWTA, _('Don\'t want to answer')),
)

CHOICES_FROM_BCPPLIST = (
    ('improved_hygiene', _('Improved hygiene')),
    ('reduced_risk_of_HIV', _('Reduced risk of HIV')),
    ('reduced_risk_of_std',
     _('reduced risk of other sexually transmitted diseases')),
    ('reduced_risk_of_cancer', _('Reduced risk of cancer')),
    ('heart_disease', _('Heart Disease or Stroke')),
    ('cancer', _('Cancer')),
    ('tb', _('Tuberculosis')),
    ('other_serious_infection', _('Other serious infection')),
    ('radio', _('Radio')),
    ('TV', _('TV')),
    ('landline_telephone', _('Landline telephone')),
    ('cell_phone', _('Cell phone')),
    ('computer', _('Computer')),
    ('access_to_internet', _('Access to internet')),
    ('refrigerator', _('Refrigerator')),
    ('condoms_consistent_use_(male_or_female)',
     _('Condoms, consistent use (male or female)')),
    ('injectable_contraceptive', _('Injectable contraceptive')),
    ('oral_contraceptive', _('Oral contraceptive')),
    ('IUD', _('IUD')),
    ('diaphragm_or_cervical_cap', _('Diaphragm or cervical cap')),
    ('rhythm_or_menstrual_cycle_timing', _('Rhythm or menstrual cycle timing')),
    ('withdrawal', _('Withdrawal')),
    ('myocardial_infarction_(heart_attack)',
     _('Myocardial infarction (heart attack)')),
    ('congestive_cardiac_failure', _('Congestive cardiac failure')),
    ('stroke_(cerebrovascular_accident,CVA)',
     _('Stroke (cerebrovascular accident, CVA)')),
    ('partner_or_spouse', _('Partner or spouse')),
    ('siblings', _('Siblings')),
    (ALONE, _('Alone')),
    ('extended_family', _('Extended family')),
    ('traditional,faith,or_religious_healer/doctor',
     _('Traditional, faith, or religious healer/doctor')),
    ('pharmacy', _('Pharmacy')),
    ('public_or_govt_health_facility_or_clinic',
     _('Public or government health facility or clinic')),
    ('private_health_facility_or_clinic',
     _('Private health facility or clinic')),
    ('community_health_worker', _('Community health worker')),
    ('water', _('Water')),
    ('sewer_(sanitation)', _('Sewer (sanitation)')),
    ('housing', _('Housing')),
    ('roads', _('Roads')),
    ('malaria', _('Malaria')),
    ('HIV/AIDS', _('HIV/AIDS')),
    ('schools', _('Schools')),
    ('unemployment', _('Unemployment')),
    ('in_this_community', _('In this community')),
    ('outside_community', _('Outside community')),
    ('farm_within', _('Farm within this community')),
    ('farm_outside_this_community', _('Farm outside this community')),
    ('cattlepost_within', _('Cattle post within this community')),
    ('cattlepost_outside', _('Cattle post outside this community')),
    ('motor_vehicle_(car,truck,taxi,etc)',
     _('Motor vehicle (car,truck,taxi, etc)')),
    ('tractor', _('Tractor')),
    ('bicycle', _('Bicycle')),
    ('motorcycle/scooter', _('Motorcycle/scooter')),
    ('donkey_or_cow_cart', _('Donkey or cow cart')),
    ('donkey/horses', _('Donkey/horses')),
)

CHRONIC_DISEASES = (
    ('diabetes', 'Diabetes'),
    ('high_bp', 'High blood pressure'),
    ('mental_illness', 'Mental Illness'),
    (OTHER, 'Other'),
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

CONTACT_TYPE = (
    ('direct', 'Direct contact with participant'),
    ('indirect', 'Contact with person other than participant'),
    ('no_contact', 'No contact made'),
)

COUNSELING_SITE = (
    ('in_home', 'In home'),
    ('mobile', 'Mobile Unit'),
    ('tent', 'Tent'),
    ('clinic', 'Clinic'),
)

DOCTOR_VISITS = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('always', _('All of the time (always)')),
    ('almost_always', _('Most of the time (almost always)')),
    ('sometimes', _('Some of the time (sometimes)')),
    ('rarely', _('Almost none of the time (rarely)')),
    ('never', _('None of the time (never)')),
    (DWTA, _('Don\'t want to answer')),
)

DXCANCER_CHOICE = (
    ('kaposi\'s_sarcoma_(KS)', 'Kaposi\'s sarcoma (KS)'),
    ('cervical_cancer', 'Cervical cancer'),
    ('breast_cancer', 'Breast cancer'),
    ('non-Hodgkin\'s_lymphoma_(NHL)', 'Non-Hodgkin\'s lymphoma (NHL)'),
    ('colorectal_cancer', 'Colorectal cancer'),
    ('prostate_cancer', 'Prostate cancer'),
    ('cancer_of_mouth,throat,voice_box_(larynx)',
     'Cancer of mouth, throat, voice box (larynx)'),
    ('cancer_of_oesophagus', 'Cancer of oesophagus'),
    (OTHER, 'Other, specify:'),
    (DWTA, 'Don\'t want to answer'),
)

EMPLOYMENT_INFO = (
    ('govt_sector', _('Yes, In the government sector')),
    ('private_sector', _('Yes, in the private sector')),
    ('self_employed_alone',
     _('Yes, self-employed working on my own')),
    ('self_employed_with_own_employees',
     _('Yes, self-employed with own employees')),
    ('not_working', _('No, not working')),
    (DWTA, _('Don\'t want to answer')),
)

ENERGY_SOURCE = (
    ('charcoal/wood', _('Charcoal/wood')),
    ('paraffin', _('Paraffin')),
    ('gas', _('Gas')),
    ('electricity_(mains)', _('Electricity (mains)')),
    ('electricity_(solar)', _('Electricity (solar)')),
    ('no_cooking_done', _('No cooking done')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

ENROLMENT_REASON = (
    ('CD4 < 50', _('Most recent (within past 3 months) CD4 < 50')),
    ('CD4 50-100', _('Most recent (within past 3 months) CD4 50-100')),
    ('AIDS_opportunistic_infection/condition',
     _('Current AIDS opportunistic infection/condition')),
)

FLOORING_TYPE = (
    ('dirt_or_earth', _('Dirt/earth ')),
    ('wood_plank', _('Wood, plank')),
    ('parquet_or_lino', _('Parquet/lino')),
    ('cement', _('Cement')),
    ('tile_flooring', _('Tile flooring')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

GRANT_TYPE = (
    ('child_support ', _('Child support ')),
    ('old_age_pension', _('Old age pension')),
    ('foster_care', _('Foster care')),
    ('disability', _('Disability (disability dependency)')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

HEALTH_CARE_PLACE = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('govt_dispensary', _('Government dispensary')),
    ('govt_health_center', _('Government health center')),
    ('govt_hospital', _('Government hospital')),
    ('christian_or_mission_health_center', _('Christian/mission health center')),
    ('Islamic_health_center', _('Islamic health center')),
    ('private_health_center_all_illnesses',
     _('Private health center for all illnesses')),
    ('private_health_center_HIV/AIDS',
     _('Private health center for HIV/AIDS')),
    ('mobile_services', _('Mobile services')),
    ('plantation_health_center', _('Plantation health center')),
    ('NGO_clinic', _('NGO clinic')),
    (DWTA, _('Don\'t want to answer')),
)

HIV_DOC_TYPE = (
    ('tebelopele', 'Tebelopele'),
    ('lab_result_form', 'Lab result form'),
    ('ART_prescription', 'ART Prescription'),
    ('PMTCT_prescription', 'PMTCT Prescription'),
    ('record_of_CD4_count', 'Record of CD4 count'),
    ('Ya_Tsie_test_card', 'Ya Tsie Test Card'),
    (OTHER, 'Other OPD card or ANC card documentation'),
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

HOUSEHOLD_INCOME = (
    ('none', _('None')),
    ('1-200_pula', _('1-200 pula')),
    ('200-499_pula', _('200-499 pula')),
    ('500-999_pula', _('500-999 pula')),
    ('1000-4999_pula', _('1000-4999 pula')),
    ('5000-10,000_pula', _('5000-10,000 pula')),
    ('10,0000-20,000_pula', _('10,0000-20,000 pula')),
    ('more_than_20,000_pula', _('More than 20,000 pula')),
    (NOT_SURE, _('I am not sure')),
    (DWTA, _('Don\'t want to answer')),
)

INTERCOURSE_TYPE = (
    ('vaginal', _('Vaginal sex')),
    ('anal', _('Anal sex')),
    ('both', _('Both vaginal and anal sex')),
)

JOB_DESCRIPTION = (
    ('farmer', _('Farmer (own land)')),
    ('farm_work', _('Farm work on employers land')),
    ('domestic', _('Domestic worker')),
    ('bar_or_hotel', _('Work in bar/ hotel/ guest house/ entertainment venue')),
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
    ('govt_worker', _('Government worker')),
    ('teacher', _('Teacher')),
    ('hcw', _('Health care worker')),
    ('other_professional', _('Other professional')),
    (DWTA, _('Don\'t want to answer')),
    (OTHER, _('Other')),
)

JOB_TYPE = (
    ('piece_job', _('Occassional or Casual employment (piece job)')),
    ('seasonal', _('Seasonal employment')),
    ('full_time', _('Formal wage employment (full-time)')),
    ('part_time', _('Formal wage employment (part-time)')),
    ('agric', _('Self-employed in agriculture')),
    ('self_full_time', _('Self-employed making money, full time')),
    ('self_part_time', _('Self-employed making money, part time')),
    (DWTA, _('Don\'t want to answer')),
    (OTHER, _('Other')),
)

MAIN_PARTNER_RESIDENCY = (
    ('this_community', _('In this community')),
    ('farm_or_cattle_post', _('On farm/cattle post')),
    ('outside_community', _('Outside this community')),
    (DWTA, _('Don\'t want to answer')),
)

#   CE001
MOBILITY = (
    ('no_problems', _('I have no problems in walking about')),
    ('slight_problems', _('I have slight problems in walking about')),
    ('moderate_problems', _('I have moderate problems in walking about')),
    ('severe_problems', _('I have severe problems in walking about')),
    ('unable_to_walk', _('I am unable to walk about')),
    (DWTA, _('Don\'t want to answer')),
)

MONTHLY_INCOME = (
    ('no_income', _('No income')),
    ('1-199_pula', _('1-199 pula')),
    ('200-499_pula', _('200-499 pula')),
    ('500-999_pula', _('500-999 pula')),
    ('1000-4999_pula', _('1000-4999 pula')),
    ('5000-10,000_pula', _('5000-10,000 pula')),
    ('more_than_10,000_pula', _('More than 10,000 pula')),
    (DWTA, _('Don\'t want to answer')),
)

NO_MEDICALCARE_REASON = (
    (NOT_APPLICABLE, 'Not applicable'),
    ('not_thinking_about_HIV_care',
     _('I am not thinking about HIV related medical/clinical '
       'care at this time')),
    ('not_ready_to_start',
     _('HIV related medical/clinical care for my HIV infection '
       'is important to me but I am not ready to start it yet')),
    ('not_found_a_doctor',
     _('I have thought about starting HIV related medical/'
       'clinical care but have not yet tried to find a doctor or clinic')),
    ('not_made_an_appointment',
     _('I have found a doctor or clinic for HIV related '
       'medical/clinical care but have not yet tried to '
       'make an appointment')),
    ('not_been_successful_yet',
     _('I have tried to obtain HIV related medical/clinical care from '
       'a doctor or clinic but have not been successful yet')),
    ('have_HIV_care_appointment',
     _('I have an appointment for HIV related medical/'
       'clinical care for my HIV infection but have not been for it yet')),
    ('do_not_know_where_to_go',
     _('I don\'t know where to go for HIV related medical/clinical care')),
    ('Do_not_have_money',
     _('I do not have the money for HIV related medical/clinical care')),
    (DWTA, _('Don\'t want to answer')),
)

OCCUPATION = (
    ('farmer', _('Farmer (own land)')),
    ('farm_worker', _('Farm worker (work on employers land)')),
    ('domestic_worker', _('Domestic Worker')),
    ('tavern_or_bar_or_entertainment', _('Work at Tavern/Bar/Entertainment Venue')),
    ('mining', _('Mining')),
    ('tourism', _('Tourism/game parks')),
    ('informal_vendors', _('Informal vendors')),
    ('commercial_sex_work', _('Commercial sex work')),
    ('transport', _('Transport (e.g., trucker)')),
    ('factory_worker', _('Factory worker')),
    ('informal_vendors', _('Informal vendors')),
    ('clerical_and_office_work', _('Clerical and office work')),
    ('small_business_or_shop_work', _('Small business/shop work')),
    ('professional', _('Professional')),
    ('fishing', _('Fishing')),
    ('uniformed_services', _('Uniformed services')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

OFF_STUDY_CODE_CHOICE = (
    ('completion_of_protocol',
     'Completion of protocol required period of time for '
     'observation (see MOP for definition of Completion.)'),
    ('death',
     'Death (complete the AF005 Death Record form)'),
    ('participant_refused',
     'Participant refused further contact (explain in Comments below)'),
    ('unable_to_contact_participant',
     'Unable to contact Participant despite repeated attempts '
     '(see MOP for definition of Lost to Follow-Up.)'),
    (OTHER, 'Other (specify)'),
)

OPPORTUNISTIC_ILLNESSES = (
    ('tuberculosis', _('Tuberculosis')),
    ('wasting', _('Wasting')),
    ('cryptococcosis', _('Cryptococcosis')),
    ('severe_bacterial_pneumonia', _('Recurrent severe bacterial pneumonia')),
    ('esophageal_candidiasis', _('Esophageal candidiasis')),
    ('pneumocystis_pneumonia', _('Pneumocystis pneumonia')),
    ('kaposi\'s_sarcoma', _('Kaposi\'s sarcoma')),
    ('cervical_cancer', _('Cervical cancer')),
    ('non-Hodgkin\'s_lymphoma', _('Non-Hodgkin\'s lymphoma')),
    ('other_record', _('Other, record')),
    ('no_current_AIDS_opportunistic_illness',
     _('No current AIDS opportunistic illness')),
)

OTHER_OCCUPATION = (
    ('none', _('None')),
    ('studying', _('Studying')),
    ('doing_housework', _('Doing housework')),
    ('looking_for_work', _('Looking for work')),
    ('doing_nothing_(not_looking_for_paid_work)',
     _('Doing nothing (not looking for paid work)')),
    ('retired_or_old_age', _('Retired/old age')),
    ('pregnant_or_recently_pregnant', _('Pregnant or recently pregnant')),
    ('sick_or_injured', _('Sick or injured')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

PAIN = (
    ('no_pain', _('I have no pain or discomfort')),
    ('slight_pain', _('I have slight pain or discomfort')),
    ('moderate_pain', _('I have moderate pain or discomfort')),
    ('severe_pain', _('I have severe pain or discomfort')),
    ('extreme_pain', _('I have extreme pain or discomfort')),
    (DWTA, _('Don\'t want to answer')),
)

PLACE_CIRC = (
    ('govt_clinic_or_hospital', _('Government clinic or hospital')),
    ('traditional_location_(Bogerwa)', _('Traditional location (Bogerwa)')),
    ('outreach_site_(mobile_or_temporary_center)',
     _('Outreach site (mobile or temporary center)')),
    ('private_practitioner', _('Private practitioner')),
    (NOT_SURE, _('I am not sure')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

REASON_UNEMPLOYED = (
    ('waiting', _('Waiting to continue agricultural work')),
    ('unemployed_looking', _('Unemployed (looking for work)')),
    ('unemployed_waiting', _('Unemployed (waiting to start new work)')),
    ('unable_to_work', _('Unable to work (permanently sick or injured)')),
    ('student', _('Student/ Apprentice/ Volunteer')),
    ('housewife', _('Housewife/ Homemaker (not looking for work)')),
    ('retired', _('Retired')),
    ('not_looking', _('Not looking for work')),
    (OTHER, _('Other')),
    (DWTA, _('Don\'t want to answer')),
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

RELATIONSHIP_TYPE = (
    ('longterm_partner', _('Longterm partner (>2 years) or spouse')),
    ('boyfriend_or_girlfriend', _('Boyfriend/Girlfriend')),
    ('casual', _('Casual (known) partner')),
    ('one _time_partner', _('One time partner (previously unknown)')),
    ('commercial_sex_worker', _('Commercial sex worker')),
    (OTHER, _('Other, specify:')),
)

SALARY = (
    ('fixed_salary', _('Fixed salary')),
    ('paid_daily', _('Paid daily')),
    ('paid_hourly', _('Paid hourly')),
    (DWTA, _('Don\'t want to answer')),
)

SELF_CARE = (
    ('no_problems', _('I have no problems washing or dressing myself')),
    ('slight_problems',
     _('I have slight problems washing or dressing myself')),
    ('moderate_problems',
     _('I have moderate problems washing or dressing myself')),
    ('severe_problems',
     _('I have severe problems washing or dressing myself')),
    ('unable_to_wash', _('I am unable to wash or dress myself')),
    (DWTA, _('Don\'t want to answer')),
)

SEX_REGULARITY = (
    ('all_the_time', _('All of the time')),
    ('sometimes', _('Sometimes')),
    ('never', _('Never')),
)

SMALLER_MEALS = (
    ('never', _('Never')),
    ('rarely', _('Rarely')),
    ('sometimes', _('Sometimes')),
    ('often', _('Often')),
    (DWTA, _('Don\'t want to answer')),
)

STI_DX = (
    ('wasting', 'Severe weight loss (wasting) - more than 10% of body weight'),
    ('diarrhoea', 'Unexplained diarrhoea for one month'),
    ('yeast_infection', 'Yeast infection of mouth or oesophagus'),
    ('pneumonia', 'Severe pneumonia or meningitis or sepsis'),
    ('PCP', 'PCP (Pneumocystis pneumonia)'),
    ('herpes', 'Herpes infection for more than one month'),
    (OTHER, 'Other'),
)

TIME_UNIT_CHOICE = (
    ('days', _('Days')),
    ('months', _('Months')),
    ('years', _('Years')),
    (DWTA, _('Don\'t want to answer')),
)

TOILET_FACILITY = (
    ('pit_latrine_within_plot', _('Pit latrine within plot')),
    ('flush_toilet_within_plot', _('Flush toilet within plot')),
    ('neighbour\'s_flush_toilet', _('Neighbour\'s flush toilet')),
    ('neighbour\'s_pit_latrine', _('Neighbour''s pit latrine')),
    ('communal_flush_toilet', _('Communal flush toilet')),
    ('communal_pit_latrine', _('Communal pit latrine')),
    ('pail_bucket_latrine', _('Pail bucket latrine')),
    ('bush', _('Bush')),
    ('river_or_other_body_of_water', _('River or other body of water')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

TRAVEL_HOURS = (
    (NONE, _('None')),
    ('Under_0.5_hour', _('Under 0.5 hour')),
    ('0.5_to_under_1_our', _('0.5 to under 1 hour')),
    ('1_to_under_2_hours', _('1 to under 2 hours')),
    ('2_to_under_3_hours', _('2 to under 3 hours')),
    ('More_than_3_hours', _('More than 3 hours')),
    (DWTA, _('Don\'t want to answer')),
)

VISIT_INFO_SOURCE = (
    ('subject', 'Subject'),
    ('other_member', 'Other household member'),
    (OTHER, _('Other, specify:')),
)

VISIT_REASON = (
    ('consent', 'Consent and Survey with subject'),
    ('absent', 'Absentee'),
    ('undecided', 'Undecided (with subject)'),
    ('refuse', 'Refusal (with subject)'),
)

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology',
     _('Routine oncology clinic visit (i.e. planned chemo, follow-up)')),
    ('ill_oncology', _('Ill oncology clinic visit')),
    ('patient_called', _('Patient called to come for visit')),
    (OTHER, _('Other, specify:')),
)

WATER_SOURCE = (
    ('communal_tap', _('Communal tap')),
    ('standpipe_or_tap_within_plot', _('Standpipe/tap within plot')),
    ('piped_indoors', _('Piped indoors')),
    ('borehole', _('Borehole')),
    ('protected_well', _('Protected well')),
    ('unprotected_or_shallow_well', _('Unprotected/shallow well')),
    ('river/dam/lake/pan', _('River /dam/lake/pan')),
    ('bowser/tanker', _('Bowser/tanker')),
    (OTHER, _('Other, specify (including unknown):')),
    (DWTA, _('Don\'t want to answer')),
)

WHEREACCESS_CHOICE = (
    ('traditional_faith_or_religious_healer/doctor',
     _('Traditional, faith, or religious healer/doctor')),
    ('pharmacy', _('Pharmacy')),
    ('public_or_govt',
     _('Public or government health facility or clinic')),
    ('private_health_facility', _('Private health facility or clinic')),
    ('community_health_worker', _('Community health worker')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

WHERECIRC_CHOICE = (
    (YES, _('Yes')),
    ('no_not_sexually_active_and_will_not_become_sexually_active',
     _('No, not sexually active and will not become sexually active')),
    ('no,prior_surgical_sterilization',
     _('No, prior surgical sterilization')),
    ('no,partner(s)_surgically_sterilized',
     _('No, partner(s) surgically sterilized')),
    ('no,post-menopause',
     _('No, post-menopause (at least 24 consecutive months without a period)')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)

WHYCIRC_CHOICE = (
    ('prevent_HIV/AIDS', _('Prevent HIV/AIDS')),
    ('other_medical_reason', _('Other medical reason')),
    ('personal_preference', _('Personal preference')),
    ('improved_hygiene', _('Improved hygiene')),
    ('cultural_tradition_and/or_religion',
     _('Cultural tradition and/or religion')),
    ('acceptance_by_sexual_partner(s)', _('Acceptance by sexual partner(s)')),
    ('acceptance_by_family, friends, and/or community',
     _('Acceptance by family, friends, and/or community')),
    (NOT_SURE, _('I am not sure')),
    (OTHER, _('Other, specify:')),
    (DWTA, _('Don\'t want to answer')),
)


YES_NO_RECORD_REFUSAL = (
    (YES, _(YES)),
    (NO, _(NO)),
    (DWTA, _('Don\'t want to answer')),
    ('record_refusal', _('Participant does not want to provide record')),
)

YES_NO_UNSURE = (
    (YES, _(YES)),
    (NO, _(NO)),
    (NOT_SURE, _('Not Sure')),
)


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

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology',
     'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'))
