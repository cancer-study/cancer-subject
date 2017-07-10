# coding: utf-8

REPORT_TYPE_CHOICE = (
        ('Original report of an event', 'Original report of an event'),
        ('Updated information', 'Updated information'),
        ('Resolution', 'Resolution'),
    )

RELATIONSHIP_DESCRIPTION_CHOICE = (
        (' Definitely related to study activities', 'Definitely related to study activities'),
        (' Probably related to study activities', 'Probably related to study activities'),
        (' Possibly related to study activities', 'Possibly related to study activities'),
        (' Probably NOT related to study activities', 'Probably NOT related to study activities'),
        (' Not related to study activities',' Not related to study activities'),
        (' Pending, cannot tell yet if related to study activities',' Pending, cannot tell '
         'yet if related to study activities'),
    )
INFO_SOURCE_CHOICE = (
        ('Clinic visit with participant', 'Clinic visit with participant'),
        ('Other contact with participant (i.e telephone call)', 'Other contact with participant'
         '(i.e telephone call)'),
        ('Contact with health care worker', 'Contact with health care worker'),
        ('Contact with family or designated person who can provide information', 'Contact with family or designated person who can provide information'),
        ('Other,specify', 'Other,specify'),
    )
PARTICIPANT_STATUS_CHOICE = (
        ('On study', 'On study'),
        ('Off study', 'Off study'),
        ('Going off study at this visit', 'Going off study at this visit'),
    )
REPORT_REASON_CHOICE = (
        ('Quarterly visit/contact (go to question 5)', 'Quarterly visit/contact (go to question 5)'),
        ('Unscheduled visit/contact (go to question 4)', 'Unscheduled visit/contact (go to question 4)'),
        ('Missed quarterly visit (go to question 5)', 'Missed quarterly visit (go to question 5)'),
        ('Lost to follow-up (use only when taking subject off study)(go to question 6)','Lost to follow-up (use only when taking subject off study)(go to question 6)'),
        ('Death (goYES_NO_DOESNT_WORK to question 6)','Death (go to question 6)'),
    )
VISIT_UNSCHEDULED_REASON_CHOICE = (
        ('Routine oncology clinic visit (i.e. planned chemo, follow-up)', 'Routine oncology clinic visit (i.e. planned chemo, follow-up)'),
        ('Ill oncology clinic visit', 'Ill oncology clinic visit'),
        ('Patient called to come for visit', 'Patient called to come for visit'),
        ('Other, specify: ', 'Other, specify: '),
    )
OFF_STUDY_CODE_CHOICE = (
        ('Completion of protocol','Completion of protocol required period of time for observation (see MOP for definition of Completion.)'),
        ('Death','Death (complete the AF005 Death Record form)'),
        ('Participant refused further contact','Participant refused further contact (explain in Comments below)'),
        ('Unable to contact Participant','Unable to contact Participant despite repeated attempts (see MOP for definition of Lost to Follow-Up.)'),
        ('Other, specify: ','Other, specify: '),
    )
PRIMARY_DEATH_CAUSE_CHOICE = (
        ('No information will ever be available (go to question 6)', 'No information will ever be available (go to question 6)'),
        ('Autopsy', 'Autopsy'),
        ('Clinical record','Clinical record'),
        ('Information from physician/nurse/other health care provider','Information from physician/nurse/other health care provider'),
        ('Information from participant’s relatives or friends','Information from participant’s relatives or friends'),
        ('Information requested, still pending','Information requested, still pending'),
        ('Other, specify: ','Other, specify: '),
    )
DEATH_CAUSE_CATEGORY_CHOICE = (
        ('No information available (go to question 6)', 'No information available (go to question 6)'),
        ('Cancer ', 'Cancer '),
        ('HIV infection or HIV/AIDS-related diagnosis','HIV infection or HIV/AIDS-related diagnosis'),
        ('Disease/injury unrelated to cancer or HIV','Disease/injury unrelated to cancer or HIV'),
        ('Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)','Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)'),
        ('Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)','Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)'),
        ('Other, specify: ','Other, specify: '),
    )
MARITAL_STATUS_CHOICE = (
        ('Single', 'Single'),
        ('Married','Married'),
        ('Cohabiting','Cohabiting'),
        ('Widowed','Widowed'),
        ('Divorced','Divorced'),
        ('Other, specify','Other, specify'),
    )
RACE_CHOICE = (
        ('Black African', 'Black African'),
        ('Caucasian', 'Caucasian'),
        ('Asian', 'Asian'),
        ('Other, specify:', 'Other, specify:'),
    )
ETHNIC_GRP_CHOICE = (
        ('Tswana-Bangwato', 'Tswana-Bangwato'),
        ('Tswana-Bakwena', 'Tswana-Bakwena'),
        ('Tswana-Bangwaketsi', 'Tswana-Bangwaketsi'),
        ('Tswana-Bakgatla', 'Tswana-Bakgatla'),
        ('Tswana-Batawana', 'Tswana-Batawana'),
        ('Tswana-Barolong', 'Tswana-Barolong'),
        ('Tswana-Bamalete', 'Tswana-Bamalete'),
        ('Tswana-Batlokwa', 'Tswana-Batlokwa'),
        ('Bakalanga', 'Bakalanga'),
        ('Basarwa', 'Basarwa'),
        ('Kgalagadi', 'Kgalagadi'),
        ('White', 'White'),
        ('Asian', 'Asian'),
        ('Other, specify:', 'Other, specify:'),
    )
DISTRICT20_CHOICE = (
        ('Central District', 'Central District'),
        ('Ghanzi District', 'Ghanzi District'),
        ('Kgalagadi District', 'Kgalagadi District'),
        ('Kgatleng District', 'Kgatleng District'),
        ('Kweneng District', 'Kweneng District'),
        ('North-East District ', 'North-East District '),
        ('North-West District (includes Chobe/Ngamiland)', 'North-West District (includes Chobe/Ngamiland)'),
        ('South-East District', 'South-East District'),
        ('Southern District', 'Southern District'),
    )
SETTING20_CHOICE = (
        ('Farm/lands', 'Farm/lands'),
        ('Village', 'Village'),
        ('City/Town', 'City/Town'),
    )
DISTRICT_CHOICE = (
        ('Central District', 'Central District'),
        ('Ghanzi District', 'Ghanzi District'),
        ('Kgalagadi District', 'Kgalagadi District'),
        ('Kgatleng District', 'Kgatleng District'),
        ('Kweneng District', 'Kweneng District'),
        ('North-East District ', 'North-East District '),
        ('North-West District (includes Chobe/Ngamiland)', 'North-West District (includes Chobe/Ngamiland)'),
        ('South-East District', 'South-East District'),
        ('Southern District', 'Southern District'),
    )
SETTING_CHOICE = (
        ('Farm/lands', 'Farm/lands'),
        ('Village', 'Village'),
        ('City/Town','City/Town'),
    )
EDUCATION_CHOICE = (
        ('None', 'None'),
        ('Primary', 'Primary'),
        ('Junior secondary', 'Junior secondary'),
        ('Senior secondary', 'Senior secondary'),
        ('Tertiary', 'Tertiary'),
    )
OCCUPATION_CHOICE = (
        ('Housewife', 'Housewife'),
        ('Salaried (government)', 'Salaried (government)'),
        ('Salaried (private)', 'Salaried (private)'),
        ('Domestic work (paid)', 'Domestic work (paid)'),
        ('Self-employed', 'Self-employed'),
        ('Student', 'Student'),
        ('Unemployed', 'Unemployed'),
        ('Other, specify:', 'Other, specify:'),
    )
MONEY_PROVIDED_CHOICE = (
        (' You', 'You'),
        (' Partner or spouse', 'Partner or spouse'),
        (' Parents', 'Parents'),
        (' Other relatives', 'Other relatives'),
        (' Friend', 'Friend'),
        ('Other, specify:', 'Other, specify:'),
    )
MONEY_EARNED_CHOICE = (
        ('None', 'None'),
        (' &lt; P200/month (&lt; P50/week)', '&lt; P200/month (&lt; P50/week)'),
        (' P200-500/month (P50-120/week)', 'P200-500/month (P50-120/week)'),
        (' P501-1000/month (P120-230/week)', 'P501-1000/month (P120-230/week)'),
        (' P1001-2500/month (P230-580/week)', 'P1001-2500/month (P230-580/week)'),
        (' P2501-5000/month (P580-1160/week)', 'P2501-5000/month (P580-1160/week)'),
        (' P5001-10000/month (P1160-2330/week)', 'P5001-10000/month (P1160-2330/week)'),
        (' P10001-20000/month (P2330-4600/week)', 'P10001-20000/month (P2330-4600/week)'),
        (' P20001-30000/month (P4600-7000/week)', 'P20001-30000/month (P4600-7000/week)'),
        (' P7000/week)',' P7000/week)'),
    )
TOILET_CHOICE = (
        (' Indoor toilet', 'Indoor toilet'),
        (' Private latrine for your house/compound', 'Private latrine for your house/compound'),
        (' Shared latrine with other compounds', 'Shared latrine with other compounds'),
        (' No latrine facilities', 'No latrine facilities'),
        (' Other, specify:', 'Other, specify:'),
    )
CANCER_TYPE_CHOICE = (
        (' Don\'t know', 'Don\'t know'),
        (' Cervical cancer', 'Cervical cancer'),
        (' Breast cancer', 'Breast cancer'),
        (' Esophageal cancer', 'Esophageal cancer'),
        (' Kaposi\'s sarcoma', 'Kaposi\'s sarcoma'),
        (' Lymphoma', 'Lymphoma'),
        (' Liver cancer', 'Liver cancer'),
        (' Eye cancer', 'Eye cancer'),
        (' Other or multiple cancers, describe:', 'Other or multiple cancers, describe:'),
    )
CANCER_BEFORE_CHOICE = (
        (' Don\'t know', 'Don\'t know'),
        (' Cervical cancer', 'Cervical cancer'),
        (' Breast cancer', 'Breast cancer'),
        (' Esophageal cancer', 'Esophageal cancer'),
        (' Kaposi\'s sarcoma', 'Kaposi\'s sarcoma'),
        (' Lymphoma', 'Lymphoma'),
        (' Leukemia', 'Leukemia'),
        (' Wilm\'s Tumor', 'Wilm\'s Tumor'),
        ('  Other or multiple cancers, describe:', 'Other or multiple cancers, describe:'),
    )
HEPATITIS_BEFORE_CHOICE = (
        (' No', 'No'),
        (' Hepatitis B', 'Hepatitis B'),
        (' Hepatitis C', 'Hepatitis C'),
        (' Don\'t know', 'Don\'t know'),
    )
HOURS_OUTDOOR_CHOICE = (
        (' 1 hour or less', '1 hour or less'),
        (' 2 hours', '2 hours'),
        (' 3 hours', '3 hours'),
        (' 4 hours', '4 hours'),
        (' 5 hours', '5 hours'),
        (' 6 hours', '6 hours'),
    )
SLEEVED_SHIRT_CHOICE = (
        (' never', 'never'),
        (' rarely', 'rarely'),
        (' sometimes', 'sometimes'),
        (' often', 'often'),
        (' always', 'always'),
    )
HAT_CHOICE = (
        (' never', 'never'),
        (' rarely', 'rarely'),
        (' sometimes', 'sometimes'),
        (' often', 'often'),
        (' always', 'always'),
    )
SHADE_UMBRELLA_CHOICE = (
        (' never', 'never'),
        (' rarely', 'rarely'),
        (' sometimes', 'sometimes'),
        (' often', 'often'),
        (' always', 'always'),
    )
SUNGLASSES_CHOICE = (
        (' never', 'never'),
        (' rarely', 'rarely'),
        (' sometimes', 'sometimes'),
        (' often', 'often'),
        (' always', 'always'),
    )
FUEL_HOUSEHOLD20_CHOICE = (
        (' solid fuels (dung, charcoal, wood, crops, coal)', 'solid fuels (dung, charcoal, wood, crops, coal)'),
        (' kerosene or gas',' kerosene or gas'),
        (' electricity',' electricity'),
        (' don’t know',' don’t know'),
        (' Other, specify',' Other, specify'),
    )
FUEL_MONTH_CHOICE = (
        (' solid fuels (dung, charcoal, wood, crops, coal)', 'solid fuels (dung, charcoal, wood, crops, coal)'),
        (' kerosene or gas',' kerosene or gas'),
        (' electricity',' electricity'),
        (' don’t know',' don’t know'),
        (' Other, specify',' Other, specify'),
    )
ASBESTOS_NO_PROTECTION_CHOICE = (
        (' less than 5 years', 'less than 5 years'),
        (' between 5 and 20 years', 'between 5 and 20 years'),
        (' more than 20 years', 'more than 20 years'),
    )
CHEMICALS_TIME_CHOICE = (
        (' less than 5 years', 'less than 5 years'),
        (' between 5 and 20 years', 'between 5 and 20 years'),
        (' more than 20 years', 'more than 20 years'),
    )
TOTAL_TIME_NO_PROTECTION_CHOICE = (
        (' less than 5 years', 'less than 5 years'),
        (' between 5 and 20 years', 'between 5 and 20 years'),
        (' more than 20 years', 'more than 20 years'),
    )
MINE_TIME_CHOICE = (
        (' less than 5 years',' less than 5 years'),
        (' between 5 and 20 years',' between 5 and 20 years'),
        (' more than 20 years',' more than 20 years'),
    )
MINE_TYPE_CHOICE = (
        (' gold',' gold'),
        (' diamond',' diamond'),
        (' copper',' copper'),
        (' nickel',' nickel'),
        (' other, specify:',' other, specify:'),
    )
MINE_UNDERGROUND_TIME_CHOICE = (
        (' less than 5 years',' less than 5 years'),
        (' between 5 and 20 years',' between 5 and 20 years'),
        (' more than 20 years',' more than 20 years'),
    )
SMOKE_NOW_CHOICE = (
        (' yes',' yes'),
        (' no, I used to smoke but quit',' no, I used to smoke but quit'),
    )
CIGARETTE_SMOKING_CHOICE = (
        (' 14 or fewer cigarettes a day',' 14 or fewer cigarettes a day'),
        (' between 15 and 25 cigarettes a day',' between 15 and 25 cigarettes a day'),
        (' more than 25 cigarettes a day',' more than 25 cigarettes a day'),
    )
CIGARETTE_SMOKED_CHOICE = (
        (' 14 or fewer cigarettes a day',' 14 or fewer cigarettes a day'),
        (' between 15 and 25 cigarettes a day',' between 15 and 25 cigarettes a day'),
        (' more than 25 cigarettes a day',' more than 25 cigarettes a day'),
    )
WHEN_QUIT_CHOICE = (
        (' less than 2 years ago',' less than 2 years ago'),
        (' between 2 and 10 years ago',' between 2 and 10 years ago'),
        (' between 10 and 20 years ago',' between 10 and 20 years ago'),
        (' more than 20 years ago',' more than 20 years ago'),
    )
AGE_FIRSTSEX_CHOICE = (
        (' younger than 15 years old',' younger than 15 years old'),
        (' between 15 and 17 years old',' between 15 and 17 years old'),
        (' older than 17 years old',' older than 17 years old'),
        (' don’t know',' don’t know'),
        (' never','never'),
    )
TRADMEDICINE_CHOICE = (
        (' Never',' Never'),
        (' Less than once a year',' Less than once a year'),
        (' Between 1 and 5 times a year',' Between 1 and 5 times a year'),
        (' Between 5 to 10 times a year',' Between 5 to 10 times a year'),
        (' More than 10 times a year',' More than 10 times a year'),
    )
CANCER_CATEGORY_CHOICE = (
        ('5 years)','5 years)'),
        ('1 year)','1 year)'),
        (' Ongoing treatment (active treatment for this cancer type in past year)',' Ongoing treatment (active treatment for this cancer type in past year)'),
    )
SYMPTOM_PROMPT_CHOICE = (
        ('Pain','Pain'),
        ('Lump/Mass','Lump/Mass'),
        ('Fever','Fever'),
        ('Cough','Cough'),
        ('Shortness of Breath','Shortness of Breath'),
        ('Bleeding','Bleeding'),
        ('Weight loss','Weight loss'),
        ('Swelling of leg','Swelling of leg'),
        ('Difficulty swallowing','Difficulty swallowing'),
        ('Bump/rash on skin or eye','Bump/rash on skin or eye'),
        ('Other','Other'),
    )
DIAGNOSIS_BASIS_CHOICE = (
        ('Clinical Only','Clinical Only'),
        ('Clinical AND Radiology (CT, X-ray, U/S)','Clinical AND Radiology (CT, X-ray, U/S)'),
        ('Surgery','Surgery'),
        ('Biochemical/Immunological Test','Biochemical/Immunological Test'),
        ('Cytology/Haematology','Cytology/Haematology'),
        ('Histology of Metastasis','Histology of Metastasis'),
        ('Histology of Primary','Histology of Primary'),
        ('Autopsy with Histology','Autopsy with Histology'),
        ('Other (including unknown): ','Other (including unknown): '),
    )
TUMOUR_BASIS_CHOICE = (
        ('Clinical','Clinical'),
        ('Pathology','Pathology'),
    )
LYMPH_BASIS_CHOICE = (
        ('Clinical','Clinical'),
        ('Pathology','Pathology'),
    )
METASTASIS_BASIS_CHOICE = (
        ('Clinical','Clinical'),
        ('Pathology','Pathology'),
    )
HEALTH_RATE_CHOICE = (
        ('Excellent','Excellent'),
        ('Very Good','Very Good'),
        ('Good','Good'),
        ('Fair','Fair'),
        ('Poor','Poor'),
        ('Very Poor','Very Poor'),
    )
HEALTH_PROBLEMS_CHOICE = (
        ('Not at all','Not at all'),
        ('Very Little','Very Little'),
        ('Somewhat','Somewhat'),
        ('Quite a lot','Quite a lot'),
        ('Could not do physical activities','Could not do physical activities'),
    )
DIFFICULTY_WORK_CHOICE = (
        ('None at all','None at all'),
        ('A little bit','A little bit'),
        ('Some','Some'),
        ('Quite a lot','Quite a lot'),
        ('Could not do daily work','Could not do daily work'),
    )
BODILY_PAIN_CHOICE = (
        ('None','None'),
        ('Very mild','Very mild'),
        ('Moderate','Moderate'),
        ('Severe','Severe'),
        ('Very serere','Very serere'),
    )
ENERGY_CHOICE = (
        ('Very much','Very much'),
        ('Quite a lot','Quite a lot'),
        ('Some','Some'),
        ('A little','A little'),
        ('None','None'),
    )
HEALTH_PROBS_LIMIT_CHOICE = (
        ('Not at all','Not at all'),
        ('Very little','Very little'),
        ('Somewhat','Somewhat'),
        ('Quite a lot','Quite a lot'),
        ('Could not do social activities','Could not do social activities'),
    )
EMOTIONAL_PROBS_CHOICE = (
        ('Not at all','Not at all'),
        ('Slightly','Slightly'),
        ('Moderately','Moderately'),
        ('Quite a lot','Quite a lot'),
        ('Extremely','Extremely'),
    )
PROBS_FROM_WORK_CHOICE = (
        ('Not at all','Not at all'),
        ('Very little','Very little'),
        ('Somewhat','Somewhat'),
        ('Quite a lot','Quite a lot'),
        ('Could not do daily activities','Could not do daily activities'),
    )
PERFORM_STATUS_CHOICE = (
        ('Asymptomatic (Fully active, able to carry on all pre-disease activities without restriction)','Asymptomatic (Fully active, able to carry on all pre-disease activities without restriction)'),
        ('Symptomatic but completely ambulatory (Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature. For example, light housework, office work)','Symptomatic but completely ambulatory (Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature. For example, light housework, office work)'),
        ('Symptomatic, &lt;50% in bed during the day (Ambulatory and capable of all self care but unable to carry out any work activities. Up and about more than 50% of waking hours)','Symptomatic, &lt;50% in bed during the day (Ambulatory and capable of all self care but unable to carry out any work activities. Up and about more than 50% of waking hours)'),
        ('50% in bed, but not bedbound (Capable of only limited self-care, confined to bed or chair 50% or more of waking hours)','50% in bed, but not bedbound (Capable of only limited self-care, confined to bed or chair 50% or more of waking hours)'),
        ('Bedbound (Completely disabled. Cannot carry on any self-care. Totally confined to bed or chair)','Bedbound (Completely disabled. Cannot carry on any self-care. Totally confined to bed or chair)'),
        ('Death','Death'),
    )
CHEMO_INTENT_CHOICE = (
        (' Curative intent',' Curative intent'),
        (' Adjuvant',' Adjuvant'),
        (' Neo-Adjuvant',' Neo-Adjuvant'),
        (' Palliative',' Palliative'),
    )
DRUG_CODE_CHOICE = (
        ('AMOX = amoxicillin','AMOX = amoxicillin'),
        ('ALLO = allopurinol','ALLO = allopurinol'),
        ('BLEO = bleomycin','BLEO = bleomycin'),
        ('CARB = carboplatin','CARB = carboplatin'),
        ('CARM = carmustine','CARM = carmustine'),
        ('CAPC = capecitabine','CAPC = capecitabine'),
        ('CIPR = ciprofloxacin','CIPR = ciprofloxacin'),
        ('CISP = cisplatin','CISP = cisplatin'),
        ('CYCL = cyclophosphamide','CYCL = cyclophosphamide'),
        ('CYTB = cytarabine','CYTB = cytarabine'),
        ('CTXM = cotrimoxazole','CTXM = cotrimoxazole'),
        ('DAUN = daunorubicin,','DAUN = daunorubicin,'),
        ('DCAR = dacarbazine','DCAR = dacarbazine'),
        ('DEXA = dexamethasone','DEXA = dexamethasone'),
        ('DOXO = doxorubicin','DOXO = doxorubicin'),
        ('DTAX = docetaxel','DTAX = docetaxel'),
        ('ETOP = etoposide','ETOP = etoposide'),
        ('FLOR = fluorouracil','FLOR = fluorouracil'),
        ('GEMC = gemcitabine','GEMC = gemcitabine'),
        ('GLEE = gleevec','GLEE = gleevec'),
        ('HYDX = hydroxyurea','HYDX = hydroxyurea'),
        ('IFOS = ifosfamide','IFOS = ifosfamide'),
        ('IRIN = irinotecan','IRIN = irinotecan'),
        ('LEUK = leukovorin','LEUK = leukovorin'),
        ('LEUP = leuprolide','LEUP = leuprolide'),
        ('LDOX = liposomal doxorubicin','LDOX = liposomal doxorubicin'),
        ('MECH = mechlorethamine','MECH = mechlorethamine'),
        ('METO = metocloperamide (maxolone)','METO = metocloperamide (maxolone)'),
        ('METX = methatrexate','METX = methatrexate'),
        ('MITO = mitoxantrone','MITO = mitoxantrone'),
        ('OXAL = oxaliplatin','OXAL = oxaliplatin'),
        ('PROC = procarbazine','PROC = procarbazine'),
        ('PROM = promethazine','PROM = promethazine'),
        ('PRED = prednisone','PRED = prednisone'),
        ('PTAX = paclitaxel','PTAX = paclitaxel'),
        ('RANT = ranitidine','RANT = ranitidine'),
        ('TAMX = tamoxifen','TAMX = tamoxifen'),
        ('VINC = vincristine','VINC = vincristine'),
        ('VINB = vinblastine','VINB = vinblastine'),
        ('VINO = vinorelbine','VINO = vinorelbine'),
        ('OTHR = other','OTHR = other'),  
    )
DOSE_CATEGORY_CHOICE = (
        ('1 = Standard','1 = Standard'),
        ('2 = Reduced Dose','2 = Reduced Dose'),
        ('3 = Other ','3 = Other '),
    )
TEST_RESULT_CHOICE = (
        ('Reactive','Reactive'),
        ('Non-Reactive','Non-Reactive'),
    )
TB_TREATMENT_CHOICE = (
        ('Yes, isoniazid preventative therapy (IPT)','Yes, isoniazid preventative therapy (IPT)'),
        ('Yes, combination anti-tuberculosis treatment (ATT)','Yes, combination anti-tuberculosis treatment (ATT)'),
    )
RECENT_RESULT_CHOICE = (
        (' Reactive (positive)',' Reactive (positive)'),
        (' Non-Reactive (negative)',' Non-Reactive (negative)'),
        (' Don\'t Know (didn\'t receive result, forgot, etc)',' Don\'t Know (didn\'t receive result, forgot, etc)'),
    )
WHO_STAGE_CHOICE = (
        ('Wasting','Wasting'),
        ('Tuberculosis','Tuberculosis'),
        ('Kaposi\'s sarcoma','Kaposi\'s sarcoma'),
        ('Kidney failure','Kidney failure'),
        ('Cryptococcal meningitis','Cryptococcal meningitis'),
        ('Severe bacterial infections','Severe bacterial infections'),
        ('Other, specify: ','Other, specify: '),
    )
CHEMO_INTENT_CHOICE = (
        (' Curative intent',' Curative intent'),
        (' Adjuvant',' Adjuvant'),
        (' Neo-Adjuvant',' Neo-Adjuvant'),
        (' Palliative',' Palliative'),
    )
WHY_DELAYED_CHOICE = (
        ('Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)','Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)'),
        ('Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.) ','Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.) '),
        ('Toxicity - renal failure (increased creatinine, swelling, etc)','Toxicity - renal failure (increased creatinine, swelling, etc)'),
        ('Toxicity - other, specify ','Toxicity - other, specify '),
        ('Cancer not responding to treatment','Cancer not responding to treatment'),
        ('Defaulted visit or lost-to-follow-up','Defaulted visit or lost-to-follow-up'),
        ('Outage of medication, supplies, laboratory results','Outage of medication, supplies, laboratory results'),
        ('Clinic too busy to accommodate','Clinic too busy to accommodate'),
        ('Other, specify ','Other, specify '),
    )
WHY_REDUCED_CHOICE = (
        ('Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)','Toxicity - hematologic (anemia, neutropenia, or thromobcytopenia)'),
        ('Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.)','Toxicity - hepatitis (jaundice, increased bilirubin, ALT/AST, etc.)'),
        ('Toxicity - renal failure (increased creatinine, swelling, etc)','Toxicity - renal failure (increased creatinine, swelling, etc)'),
        ('Toxicity - other, specify ','Toxicity - other, specify '),
        ('Cancer not responding to treatment','Cancer not responding to treatment'),
        ('Defaulted visit or lost-to-follow-up','Defaulted visit or lost-to-follow-up'),
        ('Outage of medication, supplies, laboratory results','Outage of medication, supplies, laboratory results'),
        ('Clinic too busy to accommodate','Clinic too busy to accommodate'),
        ('Dose reduced due to standard protocol (i.e. reduced intensity CHOP)','Dose reduced due to standard protocol (i.e. reduced intensity CHOP)'),
        ('Other, specify ','Other, specify '),
    )
DRUG_CODE_CHOICE = (
        ('AMOX = amoxicillin','AMOX = amoxicillin'),
        ('ALLO = allopurinol','ALLO = allopurinol'),
        ('BLEO = bleomycin','BLEO = bleomycin'),
        ('CARB = carboplatin','CARB = carboplatin'),
        ('CARM = carmustine','CARM = carmustine'),
        ('CAPC = capecitabine','CAPC = capecitabine'),
        ('CIPR = ciprofloxacin','CIPR = ciprofloxacin'),
        ('CISP = cisplatin','CISP = cisplatin'),
        ('CYCL = cyclophosphamide','CYCL = cyclophosphamide'),
        ('CYTB = cytarabine','CYTB = cytarabine'),
        ('CTXM = cotrimoxazole','CTXM = cotrimoxazole'),
        ('DAUN = daunorubicin,','DAUN = daunorubicin,'),
        ('DCAR = dacarbazine','DCAR = dacarbazine'),
        ('DEXA = dexamethasone','DEXA = dexamethasone'),
        ('DOXO = doxorubicin','DOXO = doxorubicin'),
        ('DTAX = docetaxel','DTAX = docetaxel'),
        ('ETOP = etoposide','ETOP = etoposide'),
        ('FLOR = fluorouracil','FLOR = fluorouracil'),
        ('GEMC = gemcitabine','GEMC = gemcitabine'),
        ('GLEE = gleevec','GLEE = gleevec'),
        ('HYDX = hydroxyurea','HYDX = hydroxyurea'),
        ('IFOS = ifosfamide','IFOS = ifosfamide'),
        ('IRIN = irinotecan','IRIN = irinotecan'),
        ('LEUK = leukovorin','LEUK = leukovorin'),
        ('LEUP = leuprolide','LEUP = leuprolide'),
        ('LDOX = liposomal doxorubicin','LDOX = liposomal doxorubicin'),
        ('MECH = mechlorethamine','MECH = mechlorethamine'),
        ('METO = metocloperamide (maxolone)','METO = metocloperamide (maxolone)'),
        ('METX = methatrexate','METX = methatrexate'),
        ('MITO = mitoxantrone','MITO = mitoxantrone'),
        ('OXAL = oxaliplatin','OXAL = oxaliplatin'),
        ('PROC = procarbazine','PROC = procarbazine'),
        ('PROM = promethazine','PROM = promethazine'),
        ('PRED = prednisone','PRED = prednisone'),
        ('PTAX = paclitaxel','PTAX = paclitaxel'),
        ('RANT = ranitidine','RANT = ranitidine'),
        ('TAMX = tamoxifen','TAMX = tamoxifen'),
        ('VINC = vincristine','VINC = vincristine'),
        ('VINB = vinblastine','VINB = vinblastine'),
        ('VINO = vinorelbine','VINO = vinorelbine'),
        ('OTHR = other','OTHR = other'),  
    )
DOSE_CATEGORY_CHOICE = (
        ('1 = Standard','1 = Standard'),
        ('2 = Reduced Dose','2 = Reduced Dose'),
        ('3 = Other ','3 = Other '),
    )
CANCER_RESPONSE_CHOICE = (
        ('Progressive disease (tumors are growing or new tumors are appearing)','Progressive disease (tumors are growing or new tumors are appearing)'),
        ('Stable disease (no substantial change in size or location of tumors)','Stable disease (no substantial change in size or location of tumors)'),
        ('Partial response (at least 50% decrease in tumor size, but less than 100% decrease)','Partial response (at least 50% decrease in tumor size, but less than 100% decrease)'),
        ('Complete response (all detectable cancer is gone, 100% decrease)','Complete response (all detectable cancer is gone, 100% decrease)'),
        ('Too early after treatment to assess treatment response','Too early after treatment to assess treatment response'),
        ('Cannot determine due to pending/missing/unavailable studies (labs, radiology, exam, etc.)','Cannot determine due to pending/missing/unavailable studies (labs, radiology, exam, etc.)'),
        ('Not recorded','Not recorded'),
    )
INFO_DETERMINANT_CHOICE = (
        ('Clinical exam/history','Clinical exam/history'),
        ('Radiology (X-ray, CT scan, ultrasound, etc.)','Radiology (X-ray, CT scan, ultrasound, etc.)'),
        ('Laboratory result(s) (LDH, CBC, etc.)','Laboratory result(s) (LDH, CBC, etc.)'),
        ('Pathology','Pathology'),
        ('Not recorded','Not recorded'),
    )
WHY_REFERRED_CHOICE = (
        (' IDCC (infectious disease) for HAART initiation',' IDCC (infectious disease) for HAART initiation'),
        (' IDCC (infectious disease) for modification of HAART (failure, toxicity, etc)',' IDCC (infectious disease) for modification of HAART (failure, toxicity, etc)'),
        (' GOPD, TB clinic, or local clinic for evaluation/treatment of TB',' GOPD, TB clinic, or local clinic for evaluation/treatment of TB'),
        (' Psychiatry for treatment of depression or other mental illness',' Psychiatry for treatment of depression or other mental illness'),
        (' Social work for assistance with food basket, home services, or other needs',' Social work for assistance with food basket, home services, or other needs'),
        (' Other, explain:',' Other, explain:'),
    )
HAART_STATUS_CHOICE = (
        (' Never started HAART "(skip to Question 4)"',' Never started HAART "(skip to Question 4)"'),
        (' Follow-up visit, no modifications since last visit made to HAART treatment "(skip to Question 4)"',' Follow-up visit, no modifications since last visit made to HAART treatment "(skip to Question 4)"'),
        (' Enrollment visit, patient has taken or is taking HAART "(go to Question 3, record all current and past HAART medications)"',' Enrollment visit, patient has taken or is taking HAART "(go to Question 3, record all current and past HAART medications)"'),
        (' Change in at least one antiretroviral medication (dose modification, discontinuation, temporary hold, change of medication) "(go to Question 3)"',' Change in at least one antiretroviral medication (dose modification, discontinuation, temporary hold, change of medication) "(go to Question 3)"'),
    )
MOD_REASON_CHOICE = (
        ('11 = Initiation (or re-initiation after non-adherence/stockout)','11 = Initiation (or re-initiation after non-adherence/stockout)'),
        ('12 = Toxicity decreased/resolved','12 = Toxicity decreased/resolved'),
        ('13 = Vomiting','13 = Vomiting'),
        ('14 = CNS symptoms (sleep,psych, etc)','14 = CNS symptoms (sleep,psych, etc)'),
        ('15 = Diarrhea','15 = Diarrhea'),
        ('16 = Hypersensitivity/allergic reaction','16 = Hypersensitivity/allergic reaction'),
        ('17 = Hepatotoxicity','17 = Hepatotoxicity'),
        ('18 = Neutropenia','18 = Neutropenia'),
        ('19 = Anemia','19 = Anemia'),
        ('20 = Renal failure20 = Renal failure','20 = Renal failure20 = Renal failure'),
        ('21 = Other toxicity (specify in comments)','21 = Other toxicity (specify in comments)'),
        ('22 = Virologic failure','22 = Virologic failure'),
        ('23 = Immunologic failure (CD4)','23 = Immunologic failure (CD4)'),
        ('24 = Clinical failure','24 = Clinical failure'),
        ('25 = Non-adherence','25 = Non-adherence'),
        ('26 = Interaction with cancer treatment','26 = Interaction with cancer treatment'),
        ('27 = Death','27 = Death'),
        ('28 = Other (specify in comments) ','28 = Other (specify in comments) '),
    )
ARV_REASON_CHOICE = (
        ('1 = Treatment','1 = Treatment'),
        ('2 = PMTCT','2 = PMTCT'),
        ('3 = PEP ','3 = PEP '),
    )
