from django.db import models
from edc_base.model_validators import date_not_future
from django.core.validators import RegexValidator

from edc_constants.choices import YES_NO_REFUSED, POS_NEG_REFUSED

<<<<<<< Updated upstream
from ..choices import HIV_TEST_RESULT
=======
from cancer_subject.choice import HIV_TEST_RESULT
>>>>>>> Stashed changes
from .model_mixins import CrfModelMixin


class SymptomsAndTesting (CrfModelMixin):

    """CA015"""
    # newly added form as of 09-04-2013
    """Interviewer Note: To be completed by a research assistant
        to guide subsequent"
      completion of diagnosis and other forms. If patient does
      not want to answer a "
      question, record -8."""

    symptom_prompt = models.CharField(
        verbose_name=("What symptom was most important in prompting "
                      "you to seek care leading to a diagnosis of "
                      "cancer (ie pain, lump, fever, bleeding, etc)?"),
        max_length=50,
        help_text="")

    symptom_date = models.DateField(
        verbose_name="When did you first notice the symptom that "
        "led to a diagnosis of cancer?",
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text="")
    medical_doctor_date = models.DateField(
        verbose_name="When did you first see a medical doctor "
        "for the symptom?",
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text="")
    trad_doctor_date = models.DateField(
        verbose_name="When did you first see a traditional doctor for "
        "the symptom?",
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text="")
    facility_first_seen = models.CharField(
        verbose_name="In which facility was this symptom first "
        "presented?",
        max_length=15,
        validators=[RegexValidator(
            regex=r'^[0-9]{2}[-][0-9]{1}[-][0-9]{2}$',
            message='The correct clinic facility or health-post '
            'code format is XX-X-XX'), ],
        help_text="provide name of clinic if facility code is "
        "unknown or is 00-0-00")
    facility_first_seen_other = models.CharField(
        verbose_name="Please provide name of clinic",
        max_length=35,
        null=True,
        blank=True)

    hiv_tested = models.CharField(
        verbose_name="Have you ever been tested for HIV?",
        max_length=18,
        choices=YES_NO_REFUSED,
        help_text="")
    hiv_test_result = models.CharField(
        verbose_name="What was the most recent HIV test result?",
        max_length=18,
        null=True,
        blank=True,
        choices=POS_NEG_REFUSED,
        help_text="")
    pos_date = models.DateField(
        verbose_name="When was your first positive HIV test?",
        max_length=25,
        null=True,
        blank=True,
        help_text="")
    neg_date = models.DateField(
        verbose_name="When was your last negative HIV test?",
        max_length=25,
        validators=[date_not_future],
        null=True,
        blank=True,
        help_text="if 'within the last 6 months' END form ")
    # Read to participant :It is recommended that everyone with cancer be
    # tested for HIV. We will test you now unless decide not to.
    hiv_result = models.CharField(
        verbose_name="HIV test result",
        max_length=18,
        choices=HIV_TEST_RESULT,
        help_text=("Provide appropriate post-test counselling and "
                   "referral to care. If indeterminate, send patient "
                   "to the lab for re-testing and ELISA"))
    arv_art_therapy = models.CharField(
        verbose_name="Have you ever taken anti-retroviral therapy or "
        "HAART?",
        max_length=18,
        choices=YES_NO_REFUSED,
        null=True,
        blank=True,
        help_text="if 'NO' END form")
    arv_art_start_date = models.DateField(
        verbose_name="When did you start antiretroviral therapy, "
        "or HAART",
        max_length=25,
        null=True,
        blank=True,
        help_text="")
    arv_art_now = models.CharField(
        verbose_name="Are you taking antiretroviral therapy or "
        "HAART now?",
        max_length=18,
        choices=YES_NO_REFUSED,
        null=True,
        blank=True,
        help_text="if 'Yes' END form ")
    art_art_stop_date = models.DateField(
        verbose_name="When did you most recently stop antiretroviral "
        "therapy, or HAART?",
        max_length=25,
        null=True,
        blank=True,
        help_text="")

    class Meta(CrfModelMixin.Meta):
        app_label = "cancer_subject"
        verbose_name = "Symptoms and Testing"
        verbose_name_plural = "Symptoms and Testing"
