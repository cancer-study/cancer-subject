from edc_constants.constants import OTHER, NONE, UNKNOWN
from edc_list_data import PreloadData


list_data = {
    'cancer_subject.coldflusymptoms': [
        ('cough', 'Cough'),
        ('shortness_of_breath', 'Shortness of Breath'),
        ('fever', 'Fever'),
        ('loss_of_smell', 'Sudden loss of smell'),
        ('eye_pain', 'Eye pain'),
        ('runny_nose', 'Runny nose'),
        ('sore_throat', 'Sore throat'),
    ],
    'cancer_subject.whoillness': [
        ('wasting', 'Wasting'),
        ('TB', 'Tuberculosis'),
        ('kaposi\'s_sarcoma', 'Kaposi\'s sarcoma'),
        ('kidney_failure', 'Kidney failure'),
        ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
        ('severe_bacterial_infections', 'Severe bacterial infections'),
        (OTHER, 'Other, specify')
    ],
    'cancer_subject.miningtype': [
        (' gold', ' gold'),
        (' diamond', ' diamond'),
        (' copper', ' copper'),
        (' nickel', ' nickel'),
        (' other, specify:', ' other, specify:'),
    ],

    'cancer_subject.resultstorecord': [
        ('haematology', 'Haematology'),
        ('chemistry', 'Chemistry'),
        ('tubercolosis', 'Tubercolosis'),
        (NONE, 'None')
    ],
    'cancer_subject.radiationsideeffects': [
        (UNKNOWN, 'Unknown'),
        ('hyperpigmentation', 'Hyperpigmentation'),
        ('vaginal_stenosis', 'Vaginal stenosis'),
        ('diarrhea_proctitis', 'Diarrhea, proctitis'),
        ('moist_desquamation', 'Moist desquamation'),
        ('fibrosis', 'Fibrosis'),
        (OTHER, 'Other, specify'),
        (NONE, 'None')
    ],
    'cancer_prn.deathcauseinfo': [
        ('No information will ever be available',
         'No information will ever be available'),
        ('Autopsy', 'Autopsy'),
        ('Clinical record', 'Clinical record'),
        ('Information from physician/nurse/other health care provider',
         'Information from physician/nurse/other health care provider'),
        ('Information from participant\u2019s relatives or friends',
         'Information from participant\u2019s relatives or friends'),
        ('Information requested, still pending',
         'Information requested, still pending'),
        ('Other, specify', 'Other, specify')
    ],
    'cancer_prn.causecategory': [
        ('No information will ever be available',
        'No information will ever be available'),
        ('Cancer ', 'Cancer '),
        ('HIV infection or HIV/AIDS-related diagnosis',
        'HIV infection or HIV/AIDS-related diagnosis'),
        ('Disease/injury unrelated to cancer or HIV',
        'Disease/injury unrelated to cancer or HIV'),
        ('Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)',
        'Toxicity from cancer treatment '),
        ('Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)',
        'Toxicity from HIV/AIDS treatment'),
        ('Other, specify', 'Other, specify')
    ],
}

preload_data = PreloadData(
    list_data=list_data)
