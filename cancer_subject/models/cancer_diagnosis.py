from django.core.validators import RegexValidator
from django.db import models

from edc_base.model_fields.custom_fields import OtherCharField as BaseOtherCharField
from edc_base.model_validators.date import date_not_future
from edc_base.model_fields.custom_fields import OtherCharField
from edc_constants.choices import YES_NO

from ..choices import CANCER_CATEGORY_CHOICE, DIAGNOSIS_BASIS_CHOICE
from ..choices import METASTASIS_POSSIBLE_GRADES
from ..choices import POSSIBLE_GRADES, BASIS_CHOICE
from ..choices import POSSIBLE_OVERALL_STAGES, SYMPTOM_PROMPT_CHOICE
from ..choices import POSSIBLE_OVERALL_STAGE_MODIFIER
from .list_models import ResultsToRecord
from .model_mixins import CrfModelMixin


class OtherCharField(BaseOtherCharField):
    DEFAULT_MAX_LENGTH = 250
    

class CancerDiagnosis (CrfModelMixin):

    onco_number = models.CharField(
        verbose_name='GPH ONCO number',
        max_length=10,
        null=True,
        blank=True,
    )

    pathology_number = models.CharField(
        verbose_name='Pathology number(s)',
        max_length=50,
        null=True,
        blank=True,
    )

    pm_number = models.CharField(
        verbose_name='PM number',
        max_length=10,
        null=True,
        blank=True,
    )

    diagnosis = models.CharField(
        verbose_name='Has a cancer diagnosis been made?',
        max_length=3,
        choices=YES_NO,
    )

    cancer_category = models.CharField(
        verbose_name='Category of cancer case:',
        max_length=105,
        null=True,
        blank=True,
        choices=CANCER_CATEGORY_CHOICE,
        help_text=('If patient develops a new cancer type (for example, '
                   'breast cancer after or during treatment for lymphoma) '
                   'this should be considered a new cancer case.'),
    )

    symptom_prompt = models.CharField(
        verbose_name=('What symptom was most important in prompting '
                      'patient to seek care leading to diagnosis of '
                      'cancer?'),
        max_length=25,
        null=True,
        blank=True,
        choices=SYMPTOM_PROMPT_CHOICE,
    )

    symptom_prompt_other = OtherCharField()

    symptom_first_noticed = models.DateField(
        verbose_name=('When did the patient first notice the symptom '
                      '(pain, lump, etc.) that led to diagnosis of '
                      'cancer?'),
        validators=[date_not_future],
        null=True,
        blank=True,
        max_length=25
    )

    first_evaluation = models.DateField(
        verbose_name=('When did the patient first receive an evaluation '
                      'by a doctor or nurse for the symptom that led to '
                      'diagnosis of cancer?'),
        validators=[date_not_future],
        null=True,
        blank=True,
        max_length=25
    )

    trad_evaluation = models.DateField(
        verbose_name=('When did the patient first receive an evaluation '
                      'by a \'Traditional Doctor or Sangoma\' for the '
                      'symptom that led to diagnosis of cancer?'),
        validators=[date_not_future],
        max_length=25,
        null=True,
        blank=True,
    )

    date_diagnosed = models.DateField(
        verbose_name='Date of cancer diagnosis',
        validators=[date_not_future],
        null=True,
        blank=True,
        max_length=25
    )

    diagnosis_basis = models.CharField(
        verbose_name='Basis of diagnosis',
        max_length=45,
        null=True,
        blank=True,
        choices=DIAGNOSIS_BASIS_CHOICE,
    )

    diagnosis_basis_other = OtherCharField(max_length=250,)

    diagnosis_word = models.CharField(
        verbose_name=('Diagnosis'),
        max_length=250,
        null=True,
        blank=True,
        help_text='In words, metatstatic breast cancer, kaposis of right leg',
    )

    cancer_site = models.CharField(
        verbose_name=('Cancer Site (record ICD topography code)'),
        max_length=25,
        null=True,
        blank=True,
        validators=[RegexValidator(
            regex=r'^([C](\d{2})|[C](\d{2}\.\d{1}))$',
            message='A site code always starts with a C, followed by '
            'numbers: integer or decimal.FORMAT is CXX or CXX.X'), ],
    )

    clinical_diagnosis = models.CharField(
        verbose_name=('Clinical and/or Pathologic Diagnosis (record '
                      'ICD morphology code, M9140/3)'),
        null=True,
        blank=True,
        max_length=25,
        validators=[RegexValidator(
            regex=r'^[M]{1}[0-9]{4}[/][3]{1}$',
            message='Please enter the correct morphology code. its M, '
            'followed by 4 numbers, a slash, and one more number, a '
            '3.'), ],
    )

    tumour = models.CharField(
        verbose_name='TNM system- Tumour (T)',
        max_length=15,
        null=True,
        blank=True,
        choices=POSSIBLE_GRADES,
        help_text='For Kaposi\'s record T here, 0 or 1',
    )

    tumour_basis = models.CharField(
        verbose_name='Basis of Tumour (T) assessment',
        max_length=15,
        null=True,
        blank=True,
        choices=BASIS_CHOICE,
    )

    lymph_nodes = models.CharField(
        verbose_name='TNM system- Lymph Nodes (N)',
        max_length=15,
        null=True,
        blank=True,
        choices=POSSIBLE_GRADES,
        help_text='For Kaposi\'s record I here, 0 or 1',
    )

    lymph_basis = models.CharField(
        verbose_name='Basis of Lymph Node (N) assessment',
        max_length=15,
        null=True,
        blank=True,
        choices=BASIS_CHOICE,
    )

    metastasis = models.CharField(
        verbose_name='TNM system- Metastasis (M)',
        max_length=15,
        null=True,
        blank=True,
        choices=METASTASIS_POSSIBLE_GRADES,
        help_text='For Kaposi\'s record S here, 0 or 1',
    )

    metastasis_basis = models.CharField(
        verbose_name='Basis of Metastasis (M) assessment',
        max_length=15,
        null=True,
        blank=True,
        choices=BASIS_CHOICE,
    )

    cancer_stage = models.CharField(
        verbose_name='Overall cancer stage',
        max_length=15,
        null=True,
        blank=True,
        choices=POSSIBLE_OVERALL_STAGES,
        help_text=('For lymphomas, report Ann Arbor Stage here. For '
                   'Kaposi\'s, report ACTG Stage here.'),
    )

    cancer_stage_modifier = models.CharField(
        verbose_name='Overall cancer stage modifier',
        max_length=15,
        null=True,
        blank=True,
        choices=POSSIBLE_OVERALL_STAGE_MODIFIER,
        help_text=(
            'For lymphomas, report Ann Arbor Stage here.For Kaposi\'s, '
            'report \'None\'.'),
    )

    any_other_results = models.CharField(
        verbose_name=('Are there other results of specialized testing '
                      '(receptor, cell surface markers) that should '
                      'be reported?'),
        max_length=3,
        choices=YES_NO,
        help_text='If answered YES, make sure to answer the '
        'Specialized Diagnostics form',
    )

    paper_documents = models.CharField(
        verbose_name='Folder number of stored paper documents',
        max_length=7,
    )

    results_to_record = models.ManyToManyField(
        ResultsToRecord,
        verbose_name=(
            'Based the cancer diagnosis or other factors which of '
            'the following results be recorded (refer to SOP)?'),
        blank=True,
        help_text='(tick all that apply - REMEMBER to highlight your '
        'chosen options before save)',
    )

    results_to_record_other = OtherCharField()

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Cancer Diagnosis'
        verbose_name_plural = 'Cancer Diagnosis'
