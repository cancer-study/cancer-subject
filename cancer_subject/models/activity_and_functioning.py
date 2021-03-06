from django.core.validators import (MaxValueValidator, MinValueValidator,
                                    RegexValidator)
from django.db import models
from edc_constants.choices import YES_NO, YES_NO_UNSURE_NA
from edc_constants.constants import NOT_APPLICABLE

from .list_models import ColdFluSymptoms
from .model_mixins import CrfModelMixin

from ..choices import (
    HEALTH_RATE_CHOICE, HEALTH_PROBLEMS_CHOICE,
    DIFFICULTY_WORK_CHOICE, BODILY_PAIN_CHOICE,
    ENERGY_CHOICE, HEALTH_PROBS_LIMIT_CHOICE,
    EMOTIONAL_PROBS_CHOICE, PROBS_FROM_WORK_CHOICE,
    PERFORM_STATUS_CHOICE, YES_NO_DECLINED)


class ActivityAndFunctioning (CrfModelMixin):

    """CA003"""

    health_rate = models.CharField(
        verbose_name=("1. Overall, how would you rate your health "
                      "during the PAST 4 WEEKS?"),
        max_length=15,
        choices=HEALTH_RATE_CHOICE,
        help_text="",
    )

    health_problems = models.CharField(
        verbose_name=("2. During the PAST 4 WEEKS, how much did "
                      "physical health problems limit your usual "
                      "physical activities (walking, climbing "
                      "stairs)?"),
        max_length=35,
        choices=HEALTH_PROBLEMS_CHOICE,
        help_text="",
    )

    difficulty_work = models.CharField(
        verbose_name=("3. During the PAST 4 WEEKS, how much difficulty "
                      "did you have doing your daily work, both at "
                      "home and away from home, because of your "
                      "physical health?"),
        max_length=35,
        choices=DIFFICULTY_WORK_CHOICE,
        help_text="",
    )

    bodily_pain = models.CharField(
        verbose_name=("4. How much bodily pain have you had "
                      "during the PAST 4 WEEKS?"),
        max_length=15,
        choices=BODILY_PAIN_CHOICE,
        help_text="",
    )

    probs_from_work = models.CharField(
        verbose_name=("8. During the past 4 weeks, how much did "
                      "personal or emotional problems keep you from "
                      "doing work, school or other daily activities?"),
        max_length=35,
        choices=PROBS_FROM_WORK_CHOICE,
        help_text="",
    )

    energy = models.CharField(
        verbose_name=("5. During the PAST 4 WEEKS, how much energy "
                      "did you have?"),
        max_length=15,
        choices=ENERGY_CHOICE,
        help_text="",
    )

    health_probs_limit = models.CharField(
        verbose_name=("6. During the PAST 4 WEEKS, how much did your "
                      "physical health or emotional problems limit your "
                      "usual social activities with family or friends?"),
        max_length=35,
        choices=HEALTH_PROBS_LIMIT_CHOICE,
        help_text="",
    )

    emotional_probs = models.CharField(
        verbose_name=("7. During the PAST 4 WEEKS, how much have you been "
                      "bothered by emotional problems (such as feeling "
                      "anxious, depressed or irritable)?"),
        max_length=15,
        choices=EMOTIONAL_PROBS_CHOICE,
        help_text="",
    )

    perform_status = models.CharField(
        verbose_name=("9. What is the participant perfomance status, "
                      "determined by study staff with questioning and "
                      "observation of the participant"),
        max_length=205,
        choices=PERFORM_STATUS_CHOICE,
        help_text="",
    )

    flu_symptoms = models.CharField(
        verbose_name=('10. Over the past two weeks, have you developed new '
                      'cold or flu symptoms like cough, shortness of breath, '
                      'fever, sudden loss of smell, eye pain, runny nose or '
                      'sore throat?'),
        max_length=8,
        choices=YES_NO_DECLINED,
        help_text='',
    )

    symptom_specify = models.ManyToManyField(
        ColdFluSymptoms,
        verbose_name=('11. If yes, which of these new symptoms have you '
                      'developed'),
        max_length=20,
        blank=True,
        help_text='(select all that apply)',
    )

    housemates_count = models.IntegerField(
        verbose_name='12. How many people live in your household?',
        validators=[MaxValueValidator(50), MinValueValidator(1)],
        default=1,
        help_text='Include the participant in the number',
    )

    housemate_flu_symptoms = models.CharField(
        verbose_name=('13. Over the past two weeks, has anyone in your '
                      'household developed new cold or flu symptoms like '
                      'cough, shortness of breath, fever, or sore throat?'),
        max_length=8,
        choices=YES_NO_DECLINED,
        help_text='Include the participant in patients with symptoms',
    )

    housemates_with_flu_symptoms_count = models.IntegerField(
        verbose_name='14. If yes, how many?',
        validators=[MaxValueValidator(50), MinValueValidator(1)],
        null=True,
        blank=True,
        help_text='Include the participant in the number',
    )

    closest_health_facility = models.CharField(
        verbose_name=('15. What is the closest health facility to where you '
                      'are staying now?'),
        max_length=75,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}[-][0-9]{1}[-][0-9]{2}$',
            message='The correct clinic code format is XX-X-XX'), ],
        help_text="Please give clinic code.",)

    contact_with_covid_suspect = models.CharField(
        verbose_name=('16. Have you or anyone in your household been in '
                      'contact with someone with known or suspected Covid-19?'),
        max_length=8,
        choices=YES_NO_DECLINED)

    had_covid = models.CharField(
        verbose_name='17. Have you ever had Covid-19 or a positive test?',
        max_length=8,
        choices=YES_NO_DECLINED)

    symp_dt = models.DateField(
        verbose_name=('18. When did you first have symptoms (or positive test '
                      'if no symptoms)?'),
        null=True,
        blank=True)

    pos_covid_test = models.CharField(
        verbose_name='19. Did you have positive Covid-19 test?',
        max_length=10,
        choices=YES_NO_UNSURE_NA,
        default=NOT_APPLICABLE)

    member_w_covid = models.CharField(
        verbose_name=('20. Has any member of your household other than yourself had'
                      ' Covid-19 or a positive test?'),
        max_length=8,
        choices=YES_NO_DECLINED)

    num_of_members = models.PositiveIntegerField(
        verbose_name='21. How many members of your household had a positive test?',
        null=True)

    membr_symp_dt = models.DateField(
        verbose_name=('22. When did the first household member (not yourself) '
                      'first have symptoms of Covid-19?'),
        null=True,
        blank=True)

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Activity and Functioning"
        verbose_name_plural = "Activity and Functioning"
