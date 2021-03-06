from django.db import models
from edc_base.model_fields import OtherCharField
from edc_base.model_validators.date import date_not_future
from .list_models import WhoIllness
from .model_mixins import CrfModelMixin


class BHHWhoIllness (CrfModelMixin):

    who_illness = models.ManyToManyField(
        WhoIllness,
        verbose_name='What WHO stage 3 or 4 illnesses the patient had:',
        max_length=35,
        help_text=(
            'Tick all that apply.  DO NOT include current cancer diagnosis'),
    )

    who_illness_other = OtherCharField()

    who_illness_date = models.DateField(
        verbose_name='Date of most recent WHO stage 3 or 4 illness:',
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text='DO NOT include the current cancer diagnosis.',
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'BHH: WHO illness'
        verbose_name_plural = 'BHH: WHO illness'
