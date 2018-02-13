from edc_constants.constants import DONT_KNOW, NONE, DECLINED, REFUSED
from edc_constants.constants import NEG, IND, UNK, OTHER, NEVER, PENDING
from edc_constants.constants import YES, NO, DWTA, POS


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

ASBESTOS_NO_PROTECTION_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
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

BRACHY_LENGTH = (
    ('2', '2'),
    ('3.5', '3.5'),
    ('4', '4'),
    ('6', '6'),
    ('8', '8'),
    (OTHER, 'Other'),
    (UNK, 'Unknown'),
)

BRACHY_TYPE = (
    ('T&SR', 'T&SR'),
    ('T&Ovoids', 'T&Ovoids'),
    ('T&Cylinder', 'T&Cylinder'),
    ('Cylinder', 'Cylinder'),
    ('SR', 'SR'),
    (OTHER, 'Other'),
    (UNK, 'Unknown'),
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
    (OTHER, 'Other or multiple cancers, describe:'),
)

CANCER_CATEGORY_CHOICE = (
    ('new', 'New Cancer (no treatment for this cancer type for >5 year,'
     ' or treatment began less than 6 weeks ago'),
    ('relapsed', 'Relapsed or recurrent cancer (no active treatment for'
     ' this cancer for >1 year)'),
    ('ongoing', 'Ongoing treatment (active treatment for this cancer'
     ' type in past year)'),
)

CANCER_RESPONSE = (
    ('progressive_disease', 'Progressive disease (tumors are growing '
     'or new tumors are appearing)'),
    ('stable_disease', 'Stable disease (no substantial change in size '
     'or location of tumors)'),
    ('partial_response', 'Partial response (at least 50% decrease in '
     'tumor size, but less than 100% decrease)'),
    ('complete_response', 'Complete response (all detectable cancer is'
     ' gone, 100% decrease)'),
    ('too_early_to_assess_response', 'Too early after treatment to '
     'assess treatment response'),
    ('cannot_determine_due_to_pending/missing/unavailable_studies',
     'Cannot determine due to pending/missing/unavailable studies '
     '(labs, radiology, exam, etc.)'),
    ('not_recorded', 'Not recorded'),
)

CANCER_TREATMENT_GOAL = (
    ('curative', 'Curative'),
    ('palliative', 'Palliative'),
    (UNK, 'Unknown'),
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

CHEMICALS_TIME_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)

CHEMO_INTENT = (
    ('Standard', 'Standard'),
    ('adjuvant', 'Adjuvant'),
    ('neo_adjuvant', 'Neo-Adjuvant'),
    ('concurrent_with_radiation', 'Concurrent with radiation')
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

DOSE_CATEGORY = (
    ('1', '1 = Standard'),
    ('2', '2 = Reduced Dose'),
    ('3', '3 = Other '),
)

DRUG_CODE = (
    ('AMOX', 'AMOX = amoxicillin'),
    ('ALLO', 'ALLO = allopurinol'),
    ('BLEO', 'BLEO = bleomycin'),
    ('CARB', 'CARB = carboplatin'),
    ('CARM', 'CARM = carmustine'),
    ('CAPC', 'CAPC = capecitabine'),
    ('CDX', 'CDX = casodex'),
    ('CIPR', 'CIPR = ciprofloxacin'),
    ('CISP', 'CISP = cisplatin'),
    ('CYCL', 'CYCL = cyclophosphamide'),
    ('CYTB', 'CYTB = cytarabine'),
    ('CTXM', 'CTXM = cotrimoxazole'),
    ('DAUN', 'DAUN = daunorubicin,'),
    ('DCAR', 'DCAR = dacarbazine'),
    ('DEXA', 'DEXA = dexamethasone'),
    ('DOX', 'DOXO = doxorubicin'),
    ('DTAX', 'DTAX = docetaxel'),
    ('ETOP', 'ETOP = etoposide'),
    ('FLOR', 'FLOR = fluorouracil'),
    ('GEMC', 'GEMC = gemcitabine'),
    ('GLEE', 'GLEE = gleevec'),
    ('HERC', 'HERC = herception'),
    ('HYDX', 'HYDX = hydroxyurea'),
    ('IFOS', 'IFOS = ifosfamide'),
    ('IRIN', 'IRIN = irinotecan'),
    ('LEUK', 'LEUK = leukovorin'),
    ('LEUP', 'LEUP = leuprolide'),
    ('LDOX', 'LDOX = liposomal doxorubicin'),
    ('MECH', 'MECH = mechlorethamine'),
    ('METO', 'METO = metocloperamide (maxolone)'),
    ('METX', 'METX = methatrexate'),
    ('MITO', 'MITO = mitoxantrone'),
    ('OXAL', 'OXAL = oxaliplatin'),
    ('PROC', 'PROC = procarbazine'),
    ('PROM', 'PROM = promethazine'),
    ('PRED', 'PRED = prednisone'),
    ('PTAX', 'PTAX = paclitaxel'),
    ('RANT', 'RANT = ranitidine'),
    ('RITX', 'RITX = Rituximab'),
    ('TAMX', 'TAMX = tamoxifen'),
    ('VINC', 'VINC = vincristine'),
    ('VINB', 'VINB = vinblastine'),
    ('VINO', 'VINO = vinorelbine'),
    ('ZDX', 'ZDX = zoladex'),
    ('OTHR', 'OTHR = other'),
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
    ('rarely', 'Rarely'),
    ('sometimes', 'Sometimes'),
    ('often', 'Often'),
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
     'Follow-up visit, no modifications since last visit made to '
     'HAART treatment "(skip to Question 4)"'),
    ('enrollment_visit', 'Enrollment visit, patient has taken or '
     'is taking HAART "(go to Question 3, record all current and '
     'past HAART medications)"'),
    ('change_in_at_least_one_antiretroviral_medication',
     'Change in at least one antiretroviral medication (dose '
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

HIV_TEST_RESULT = (
    (POS, 'Positive (both rapid tests)'),
    (NEG, 'Negative (both rapid tests)'),
    (IND, 'Indeterminate (different results on rapid tests)'),
    (PENDING, 'Result pending (sent to lab waiting for result)'),
    (REFUSED, 'Patient refuses HIV testing today'),
)

HOURS_OUTDOOR_CHOICE = (
    ('1_hour_or_less', '1 hour or less'),
    ('2_hours', '2 hours'),
    ('3_hours', '3 hours'),
    ('4_hours', '4 hours'),
    ('5_hours', '5 hours'),
    ('6_hours', '6 hours'),
)

INFO_SOURCE_CHOICE = (
    ('clinic_visit', 'Clinic visit with participant'),
    ('other_contact_with_participant', 'Other contact with participant'
     '(i.e telephone call)'),
    ('health_care_worker', 'Contact with health care worker'),
    ('family_or_designated_person_who_can_provide_information',
     'Contact with family or designated person who can provide information'),
    (OTHER, 'Other, specify:'),
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

MODIFIER = (
    ('X', 'X'),
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
)

MODALITY = (
    ('photons', 'Photons'),
    ('electrons', 'Electrons'),
    ('brachy', 'Brachy'),
    ('particle_therapy', 'Particle Therapy'),
    (OTHER, 'Other Energy'),
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

NUMBER_OF_CHEMO_CYLCES = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    (OTHER, 'other'),
    (UNK, 'unknown'),
)

NUMBER_OF_CHEMO_INTERVALS = (
    ('1 week', '1 week'),
    ('2 weeks', '2 weeks'),
    ('3 weeks', '3 weeks'),
    ('4 weeks', '4 weeks'),
    (OTHER, 'other'),
    (UNK, 'unknown'),
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

PATIENT_FOLLOW_UP = (
    ('PMH', 'Princess Marina Hospital'),
    ('NRH', 'Nyangabgwe Referral Hospital'),
    ('SEROWE', 'Serowe'),
    ('MAUN', 'Maun'),
    (OTHER, 'Other, specify:'),
)


PARTICIPANT_STATUS_CHOICE = (
    ('on_study', 'On study'),
    ('off_study', 'Off study'),
    ('going_off_study_at_this_visit', 'Going off study at this visit'),
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

RADIATION_TECHNIQUE = (
    ('AP/PA', 'AP/PA'),
    ('4_field_box', '4-field Box'),
    ('opposed_laterals', 'Opposed Laterals'),
    ('tangents', 'Tangents'),
    ('IMRT', 'IMRT'),
    ('IR_192', 'IR 192'),
    (OTHER, 'Other Technique')
)

RACE_CHOICE = (
    ('black_african', 'Black African'),
    ('caucasian', 'Caucasian'),
    ('asian', 'Asian'),
    (OTHER, 'Other, specify:'),
)

REASONS_MISSED_OR_DELAYED = (
    ('toxicity_hematologic', 'Toxicity- hematologic (anemia, neutropenia, or low plts), '),
    ('toxicity_skin', 'Toxicity-skin (dermatitis, mucositis), '),
    ('unresponsive', 'Cancer not responding to treatment'),
    ('defaulted', 'Defaulted visit or lost to follow-up'),
    ('machine_downtime', 'Machine down-time or repair'),
    ('no_accomodation', 'clinic too busy to accommodate'),
    ('no_transport', 'lack of transportation to facility'),
    (OTHER, 'Other, specify'),
)

RELATIONSHIP_DESCRIPTION_CHOICE = (
    ('definitely_related',
        'Definitely related to study activities'),
    ('probably_related',
        'Probably related to study activities'),
    ('possibly_related',
        'Possibly related to study activities'),
    ('probably_NOT_related',
        'Probably NOT related to study activities'),
    ('not_related',
     'Not related to study activities'),
    ('pending,cannot_tell_yet_if_related',
     'Pending, cannot tell yet if related to study activities'),
)

REPORT_TYPE_CHOICE = (
    ('original_report', 'Original report of an event'),
    ('updated_information', 'Updated information'),
    ('resolution', 'Resolution'),
)

REPORT_REASON_CHOICE = (
    ('quarterly_visit/contact',
     'Quarterly visit/contact (go to question 5)'),
    ('unscheduled_visit/contact',
     'Unscheduled visit/contact (go to question 4)'),
    ('missed_quarterly_visit',
     'Missed quarterly visit (go to question 5)'),
    ('lost_to_follow-up',
     'Lost to follow-up (use only when taking subject off study)(go to question 6)'),
    ('Death', 'Death (go to question 6)'),
    ('off_study', 'Off study'),
    ('deferred', 'Deferred'),
)

RESPONSE = (
    (UNK, 'Unknown'),
    ('complete', 'Complete'),
    ('almost_complete', 'Almost Complete'),
    ('residual_tumor', 'Residual Tumor'),
    ('poor_response', 'Poor response'),
    ('good_palliation', 'Good palliation'),
    ('modest_palliation', 'Modest Palliation'),
    ('poor_palliation', 'Poor Palliation'),
    (OTHER, 'Other, specify'),
)

SETTING_CHOICE = (
    ('farm/lands', 'Farm/lands'),
    ('village', 'Village'),
    ('city/town', 'City/Town'),
)

SIDE_EFFECTS = (
    (UNK, 'Unknown'),
    ('hyperpigmentation', 'hyperpigmentation'),
    ('vaginal_stenosis', 'vaginal stenosis'),
    ('diarrhea_proctitis', 'diarrhea, proctitis'),
    ('moist_desquamation', 'moist desquamation'),
    ('fibrosis', 'fibrosis'),
    (OTHER, 'Other, specify'),
)

SMOKE_NOW_CHOICE = (
    (YES, YES),
    (NO, 'no, I used to smoke but quit'),
)

STAGES = (
    ('X', 'X'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
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
    (POS, 'Reactive'),
    (NEG, 'Non-Reactive'),
)

TOILET_CHOICE = (
    ('indoor_toilet', 'Indoor toilet'),
    ('private_latrine', 'Private latrine for your house/compound'),
    ('shared_latrine', 'Shared latrine with other compounds'),
    ('no_latrine', 'No latrine facilities'),
    (OTHER, 'Other, specify:'),
)

TOTAL_TIME_NO_PROTECTION_CHOICE = (
    ('<5 years', 'less than 5 years'),
    ('5 to 20 years', 'between 5 and 20 years'),
    ('>20 years', 'more than 20 years'),
)

TRADMEDICINE_CHOICE = (
    (NEVER, 'Never'),
    ('less_than_once_yearly', 'Less than once a year'),
    ('between_1_and_5_times_yearly', 'Between 1 and 5 times a year'),
    ('between_5_to_10_times_yearly', 'Between 5 to 10 times a year'),
    ('more_than_10_times_yearly', 'More than 10 times a year'),
    (DECLINED, 'Patient declined to answer'),
)

TREATMENT_INTENT = (
    (UNK, 'Unknown'),
    ('curative', 'Curative'),
    ('palliative', 'Palliative'),
)

TREATMENT_RELATIONSHIP = (
    (UNK, 'Unknown'),
    ('no_modalities', 'No other treatment modalities'),
    ('concurrent_chemo', 'Concurrent chemotherapy'),
    ('adj_after_surgery', 'Adjuvant after surgery'),
    ('adj_after_chemo', 'Adjuvant after chemotherapy'),
    ('adj_after_surgery_and_chemo', 'Adjuvant after surgery and chemotherapy'),
    ('neo_before_chemo', 'Neoadjuvant before Chemotherapy'),
    ('neo_before_surgery', 'Neoadjuvant before Surgery'),
    (OTHER, 'Other, specify'),
)

VISIT_UNSCHEDULED_REASON = (
    ('routine_oncology', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
    ('ill_oncology', 'Ill oncology clinic visit'),
    ('patient_called', 'Patient called to come for visit'),
    (OTHER, 'Other, specify:'),
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

WHY_DELAYED = (
    ('heme_tox', 'Toxicity - hematologic (anemia, neutropenia,'
     ' or thromobcytopenia)'),
    ('hepato_tox', 'Toxicity - hepatitis (jaundice, increased '
     'bilirubin, ALT/AST, etc.) '),
    ('renal_tox', 'Toxicity - renal failure (increased creatinine,'
     ' swelling, etc)'),
    ('other_tox', 'Toxicity - other, specify '),
    ('no_response', 'Cancer not responding to treatment'),
    ('default', 'Defaulted visit or lost-to-follow-up'),
    ('outage', 'Outage of medication, supplies, laboratory results'),
    ('clinic_busy', 'Clinic too busy to accommodate'),
    (OTHER, 'Other, specify:'),
)

WHY_REDUCED = (
    ('heme_tox', 'Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)'),
    ('hepat_tox', 'Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.)'),
    ('rena_tox', 'Toxicity - renal failure (increased creatinine, swelling, etc)'),
    ('othe_tox', 'Toxicity - other, specify '),
    ('no_response', 'Cancer not responding to treatment'),
    ('default', 'Defaulted visit or lost-to-follow-up'),
    ('outage', 'Outage of medication, supplies, laboratory results'),
    ('clinic_busy', 'Clinic too busy to accommodate'),
    ('standard_protocol', 'Dose reduced due to standard protocol (i.e. '
     'reduced intensity CHOP)'),
    (OTHER, 'Other, specify:'),
)

WHY_REFERRED = (
    ('IDCC_for_HAART_initiation', ' IDCC (infectious disease) '
     'for HAART initiation'),
    ('IDCC_for_modification_of_HAART', ' IDCC (infectious disease) '
     'for modification of HAART (failure, toxicity, etc)'),
    ('GOPD,TB_clinic,or_local_clinic_for_evaluation/treatment_of_TB',
     'GOPD, TB clinic, or local clinic for evaluation/treatment of TB'),
    ('psychiatry_for_treatment_of_depression_or_other_mental_illness',
     ' Psychiatry for treatment of depression or other mental illness'),
    ('social_work_for_assistance_with_food_basket,home_services,or_other_needs',
     ' Social work for assistance with food basket, home services, or other needs'),
    (OTHER, ' Other, explain:'),
)

YES_NO_DECLINED = (
    (YES, YES),
    (NO, NO),
    (DECLINED, 'Patient declined to answer')
)

YES_NO_DOESNT_WORK = (
    ('YES', 'Yes'),
    ('NO', 'Yes'),
    ('doesnt_work', 'Doesn\'t work'),
)
