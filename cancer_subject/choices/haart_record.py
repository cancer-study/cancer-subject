HAART_STATUS_CHOICE = (
    (' Never started HAART "(skip to Question 4)"', ' Never started HAART "(skip to Question 4)"'),
    (' Follow-up visit, no modifications since last visit made to HAART treatment "(skip to Question 4)"', ' Follow-up visit, no modifications since last visit made to HAART treatment "(skip to Question 4)"'),
    (' Enrollment visit, patient has taken or is taking HAART "(go to Question 3, record all current and past HAART medications)"', ' Enrollment visit, patient has taken or is taking HAART "(go to Question 3, record all current and past HAART medications)"'),
    (' Change in at least one antiretroviral medication (dose modification, discontinuation, temporary hold, change of medication) "(go to Question 3)"', ' Change in at least one antiretroviral medication (dose modification, discontinuation, temporary hold, change of medication) "(go to Question 3)"'),
)
MOD_REASON_CHOICE = (
    ('11 = Initiation (or re-initiation after non-adherence/stockout)', '11 = Initiation (or re-initiation after non-adherence/stockout)'),
    ('12 = Toxicity decreased/resolved', '12 = Toxicity decreased/resolved'),
    ('13 = Vomiting', '13 = Vomiting'),
    ('14 = CNS symptoms (sleep,psych, etc)', '14 = CNS symptoms (sleep,psych, etc)'),
    ('15 = Diarrhea', '15 = Diarrhea'),
    ('16 = Hypersensitivity/allergic reaction', '16 = Hypersensitivity/allergic reaction'),
    ('17 = Hepatotoxicity', '17 = Hepatotoxicity'),
    ('18 = Neutropenia', '18 = Neutropenia'),
    ('19 = Anemia', '19 = Anemia'),
    ('20 = Renal failure20 = Renal failure', '20 = Renal failure20 = Renal failure'),
    ('21 = Other toxicity (specify in comments)', '21 = Other toxicity (specify in comments)'),
    ('22 = Virologic failure', '22 = Virologic failure'),
    ('23 = Immunologic failure (CD4)', '23 = Immunologic failure (CD4)'),
    ('24 = Clinical failure', '24 = Clinical failure'),
    ('25 = Non-adherence', '25 = Non-adherence'),
    ('26 = Interaction with cancer treatment', '26 = Interaction with cancer treatment'),
    ('27 = Death', '27 = Death'),
    ('28 = Other (specify in comments) ', '28 = Other (specify in comments) '),
)
ARV_REASON_CHOICE = (
    ('1 = Treatment', '1 = Treatment'),
    ('2 = PMTCT', '2 = PMTCT'),
    ('3 = PEP ', '3 = PEP '),
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
