# coding: utf-8
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from edc_constants.choices import YES_NO_DONT_KNOW

from .model_mixins import CrfModelMixin


class BaseRiskAssessmentEating (CrfModelMixin):

    """ eating """
    five_fruit = models.CharField(
        verbose_name=('Do you eat 5 or more fruit, vegetables, or '
                      'beans per day?'),
        max_length=25,
        choices=YES_NO_DONT_KNOW,
        help_text=('One serving is one apple, banana or orange, 1 cup '
                   'of raw leafy vegetable (like spinach or lettuce), '
                   '1/2 cup of beans/peas, 1/2 cup of  chopped, '
                   'cooked or canned fruit/vegetable, or 3/4 cup of '
                   'fruit/vegetable juice. Any fruit, vegetable, or '
                   'beans qualify.'),
    )

    meals_weekly = models.IntegerField(
        verbose_name='How many meals per week include corn/maize?',
        validators=[MinValueValidator(0), MaxValueValidator(30)],
    )

    meal_sorghum = models.IntegerField(
        verbose_name='How many meals per week include sorghum?',
        validators=[MinValueValidator(0), MaxValueValidator(30)],
    )

    meal_millet = models.IntegerField(
        verbose_name='How many meals per week include millet?',
        validators=[MinValueValidator(0), MaxValueValidator(30)],
    )

    meal_rice = models.IntegerField(
        verbose_name='How many meals per week include rice?',
        validators=[MinValueValidator(0), MaxValueValidator(30)],
    )

    meal_peanuts = models.IntegerField(
        verbose_name=('How many meals per week include '
                      'peanuts/groundnuts?'),
        validators=[MinValueValidator(0), MaxValueValidator(30)],
    )

    class Meta(CrfModelMixin.Meta):
        app_label = 'cancer_subject'
        verbose_name = 'Base Risk Assessment: Eating'
        verbose_name_plural = 'Base Risk Assessment: Eating'
