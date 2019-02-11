from django.db import models
from edc_base.model_validators.date import date_not_future

from ..choices import CANCER_RESPONSE
from .list_models import InfoDeterminant
from .model_mixins import CrfModelMixin


# from ..cancer_list.models import InfoDeterminant
class TreatmentResponse (CrfModelMixin):

    tx_response_class = models.CharField(
        verbose_name='Response to cancer treatment as classified '
        'by oncologist / doctor?',
        max_length=95,
        choices=CANCER_RESPONSE,)

    tx_info_determinant = models.ManyToManyField(
        InfoDeterminant,
        verbose_name='Information used by oncologist / doctor '
        'to determine treatment response?',
        max_length=45,)

    tx_response_date = models.DateField(
        verbose_name='Date of assessment of treatment response:',
        max_length=25,
        validators=[date_not_future])

    tx_response = models.TextField(
        verbose_name=('Briefly describe response to treatment and '
                      'information used to judge '
                      'treatment response: '),
        max_length=350,)

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Treatment Response'
