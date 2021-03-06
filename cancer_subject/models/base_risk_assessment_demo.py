from django.core.validators import MinValueValidator
from django.db import models
from edc_base.model_fields.custom_fields import OtherCharField
from edc_constants.choices import YES_NO

from ..choices import (MARITAL_STATUS_CHOICE, MONEY_PROVIDED_CHOICE,
                       OCCUPATION_CHOICE)
from ..choices import DISTRICT_CHOICE, COMMUNITY, EDUCATION_CHOICE
from ..choices import ETHNIC_GRP_CHOICE, FOOD_SECURITY, MONEY_EARNED_CHOICE
from ..choices import SETTING_CHOICE, TOILET_CHOICE, RACE_CHOICE
from .model_mixins import CrfModelMixin


class BaseRiskAssessmentDemo (CrfModelMixin):

    marital_status = models.CharField(
        verbose_name='Marital status:',
        max_length=15,
        choices=MARITAL_STATUS_CHOICE,
    )
    marital_status_other = OtherCharField()

    race = models.CharField(
        verbose_name='Race:',
        max_length=50,
        choices=RACE_CHOICE,
    )

    race_other = OtherCharField()

    ethnic_grp = models.CharField(
        verbose_name='Ethnic Group:',
        max_length=25,
        choices=ETHNIC_GRP_CHOICE,
    )

    ethnic_grp_other = OtherCharField()

    # added in upgrade
    community = models.CharField(
        verbose_name='Since 2014, what community have you lived in?',
        max_length=35,
        choices=COMMUNITY,
    )
    community_other = OtherCharField()

    district20 = models.CharField(
        verbose_name=('Over the past 20 years, which district have '
                      'you lived in the most?'),
        max_length=55,
        choices=DISTRICT_CHOICE,
    )

    setting20 = models.CharField(
        verbose_name=('Over the past 20 years, what best describes '
                      'the setting you have lived in for most of '
                      'the time?'),
        max_length=15,
        choices=SETTING_CHOICE,
    )

    district = models.CharField(
        verbose_name='Which district do you live in now?',
        max_length=65,
        choices=DISTRICT_CHOICE,
    )

    setting = models.CharField(
        verbose_name=('What best describes the setting you live in '
                      'for most of the time now?'),
        max_length=15,
        choices=SETTING_CHOICE,
    )

    education = models.CharField(
        verbose_name='Educational level completed:',
        max_length=25,
        choices=EDUCATION_CHOICE,
    )

    occupation = models.CharField(
        verbose_name='Occupation:',
        max_length=25,
        choices=OCCUPATION_CHOICE,
    )
    occupation_other = OtherCharField()

    money_provide = models.CharField(
        verbose_name='Who provides most of your money:',
        max_length=25,
        choices=MONEY_PROVIDED_CHOICE,
    )
    money_provide_other = OtherCharField()

    money_earned = models.CharField(
        verbose_name='How much money do you personally earn?',
        max_length=45,
        choices=MONEY_EARNED_CHOICE,
    )

    electricity = models.CharField(
        verbose_name='Do you have electricity in your house?',
        max_length=3,
        choices=YES_NO,
    )

    toilet = models.CharField(
        verbose_name=('Which of the following types of toilet '
                      'facilities do you most often use at home?'),
        max_length=45,
        choices=TOILET_CHOICE,
    )

    toilet_other = OtherCharField()

    household_people = models.IntegerField(
        verbose_name=('How many people, including yourself, stay in '
                      'your household/compound most of the time?'),
        validators=[MinValueValidator(1)],
        null=True,
        blank=True)

    food_security = models.CharField(
        verbose_name=('In the past 4 weeks, did you or any household '
                      'member have to eat a smaller meal than you '
                      'felt you needed, or even to skip a meal, '
                      'because there was not enough food?'),
        max_length=15,
        choices=FOOD_SECURITY,
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Base Risk Assessment: Demographics'
        verbose_name_plural = 'Base Risk Assessment: Demographics'
