from edc_constants.constants import OTHER, NONE, UNKNOWN
from edc_list_data import PreloadData


list_data = {
    'cancer_subject.whoillness': [
        ('wasting', 'Wasting'),
        ('TB', 'Tuberculosis'),
        ('kaposi\'s_sarcoma', 'Kaposi\'s sarcoma'),
        ('kidney_failure', 'Kidney failure'),
        ('cryptococcal_meningitis', 'Cryptococcal meningitis'),
        ('severe_bacterial_infections', 'Severe bacterial infections'),
        (OTHER, 'Other, specify')
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
}

preload_data = PreloadData(
    list_data=list_data)
