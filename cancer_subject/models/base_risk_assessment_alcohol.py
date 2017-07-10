from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


from .model_mixins import CrfModelMixin


class BaseRiskAssessmentAlcohol (CrfModelMixin):

    alcohol_weekly = models.IntegerField(
        verbose_name=("How many days per week do you drink alcohol?"),
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        # blank = True,
        help_text="",)

    amount_drinking = models.IntegerField(
        verbose_name=("On days you drink, how many drinks do you have (one drink is 300ml of "
                      "beer/chibuku, 150ml of wine,or 50ml of whiskey/vodka/gin)?"),
        validators=[MinValueValidator(1), MaxValueValidator(100)],
        # blank = True,
        help_text="",)

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Base Risk Assessment: Alcohol"
        verbose_name_plural = "Base Risk Assessment: Alcohol"
