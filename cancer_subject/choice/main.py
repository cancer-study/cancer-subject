# coding: utf-8
from edc_constants.constants import YES


PRIMARY_DEATH_CAUSE_CHOICE = (
    ('No information will ever be available (go to question 6)',
     'No information will ever be available (go to question 6)'),
    ('Autopsy', 'Autopsy'),
    ('Clinical record', 'Clinical record'),
    ('Information from physician/nurse/other health care provider',
     'Information from physician/nurse/other health care provider'),
    ('Information from participant’s relatives or friends',
     'Information from participant’s relatives or friends'),
    ('Information requested, still pending',
     'Information requested, still pending'),
    ('Other, specify: ', 'Other, specify: '),
)
DEATH_CAUSE_CATEGORY_CHOICE = (
    ('No information available (go to question 6)',
     'No information available (go to question 6)'),
    ('Cancer ', 'Cancer '),
    ('HIV infection or HIV/AIDS-related diagnosis',
     'HIV infection or HIV/AIDS-related diagnosis'),
    ('Disease/injury unrelated to cancer or HIV',
     'Disease/injury unrelated to cancer or HIV'),
    ('Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)',
     'Toxicity from cancer treatment (complications of chemotherapy, radiation, or surgery)'),
    ('Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)',
     'Toxicity from HIV/AIDS treatment (HAART or treatment of HIV/AIDS-related diagnosis)'),
    ('Other, specify: ', 'Other, specify: '),
)

CANCER_CATEGORY_CHOICE = (
    ('5 years)', '5 years)'),
    ('1 year)', '1 year)'),
    (' Ongoing treatment (active treatment for this cancer type in past year)',
     ' Ongoing treatment (active treatment for this cancer type in past year)'),
)

PERFORM_STATUS_CHOICE = (
    ('Asymptomatic (Fully active, able to carry on all pre-disease activities without restriction)',
     'Asymptomatic (Fully active, able to carry on all pre-disease activities without restriction)'),
    ('Symptomatic but completely ambulatory (Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature. For example, light housework, office work)',
     'Symptomatic but completely ambulatory (Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature. For example, light housework, office work)'),
    ('Symptomatic, &lt;50% in bed during the day (Ambulatory and capable of all self care but unable to carry out any work activities. Up and about more than 50% of waking hours)',
     'Symptomatic, &lt;50% in bed during the day (Ambulatory and capable of all self care but unable to carry out any work activities. Up and about more than 50% of waking hours)'),
    ('50% in bed, but not bedbound (Capable of only limited self-care, confined to bed or chair 50% or more of waking hours)',
     '50% in bed, but not bedbound (Capable of only limited self-care, confined to bed or chair 50% or more of waking hours)'),
    ('Bedbound (Completely disabled. Cannot carry on any self-care. Totally confined to bed or chair)',
     'Bedbound (Completely disabled. Cannot carry on any self-care. Totally confined to bed or chair)'),
    ('Death', 'Death'),
)

RECENT_RESULT_CHOICE = (
    (' Reactive (positive)', ' Reactive (positive)'),
    (' Non-Reactive (negative)', ' Non-Reactive (negative)'),
    (' Don\'t Know (didn\'t receive result, forgot, etc)',
     ' Don\'t Know (didn\'t receive result, forgot, etc)'),
)


CANCER_RESPONSE_CHOICE = (
    ('Progressive disease (tumors are growing or new tumors are appearing)',
     'Progressive disease (tumors are growing or new tumors are appearing)'),
    ('Stable disease (no substantial change in size or location of tumors)',
     'Stable disease (no substantial change in size or location of tumors)'),
    ('Partial response (at least 50% decrease in tumor size, but less than 100% decrease)',
     'Partial response (at least 50% decrease in tumor size, but less than 100% decrease)'),
    ('Complete response (all detectable cancer is gone, 100% decrease)',
     'Complete response (all detectable cancer is gone, 100% decrease)'),
    ('Too early after treatment to assess treatment response',
     'Too early after treatment to assess treatment response'),
    ('Cannot determine due to pending/missing/unavailable studies (labs, radiology, exam, etc.)',
     'Cannot determine due to pending/missing/unavailable studies (labs, radiology, exam, etc.)'),
    ('Not recorded', 'Not recorded'),
)


APPOINTMENT_REASON = (
    ('routine', 'Routine'),
)
