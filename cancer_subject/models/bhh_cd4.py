from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .model_mixins import CrfModelMixin


class BHHCd4 (CrfModelMixin):

    nadir_cd4 = models.DecimalField(
        verbose_name='What is the value of the lowest \'CD4\' test recorded?',
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        null=True,
        help_text=('If current (most recent) CD4 is lowest recorded, '
                   'record again here.'),
    )

    nadir_cd4_drawn_date = models.DateField(
        verbose_name='Date \'CD4\' test was run:',
        max_length=25,
        null=True,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'BHH: CD4'
        verbose_name_plural = 'BHH: CD4'
