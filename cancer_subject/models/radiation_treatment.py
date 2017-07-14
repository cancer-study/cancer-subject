from django.db import models

from edc_constants.choices import YES_NO_UNKNOWN
from edc_base.model_fields import OtherCharField

from .model_mixins import CrfModelMixin

from .list_models import RadiationSideEffects
from ..choices.radiation_treatment import (
    STAGES, MODIFIER, TREATMENT_INTENT,
    TREATMENT_RELATIONSHIP, RESPONSE,
    REASONS_MISSED_OR_DELAYED, RADIATION_TECHNIQUE,
    MODALITY, BRACHY_LENGTH, BRACHY_TYPE)
from edc_base.model_mixins.base_uuid_model import BaseUuidModel


class RadiationTreatment (CrfModelMixin):

    treatment_start_date = models.DateField(
        verbose_name="Treatment start date",
        null=True,
        blank=True,
        max_length=25,
        help_text="",
    )

    treatment_end_date = models.DateField(
        verbose_name="Treatment end date",
        null=True,
        blank=True,
        max_length=25,
        help_text="",
    )

    tumour_stages = models.CharField(
        verbose_name="TNM system- Tumour (T) stage recorded in "
        "radiation records:",
        max_length=15,
        null=True,
        blank=True,
        choices=STAGES,
        help_text="For Kaposi's record T here, 0 or 1",
    )

    lymph_stages = models.CharField(
        verbose_name="TNM system- Lymph Nodes (N) stage recorded in "
        "radiation records:",
        max_length=15,
        null=True,
        blank=True,
        choices=STAGES,
        help_text="For Kaposi's record I here, 0 or 1",
    )

    metastasis_stages = models.CharField(
        verbose_name="TNM system- Metastasis (M) stage recorded in "
        "radiation records:",
        max_length=15,
        null=True,
        blank=True,
        choices=STAGES,
        help_text="For Kaposi's record S here, 0 or 1",
    )

    overall_stages = models.CharField(
        verbose_name="Overall cancer stage",
        max_length=15,
        null=True,
        blank=True,
        choices=STAGES,
        help_text=("For lymphomas, report Ann Arbor Stage here. "
                   "For Kaposi's, report "
                   "ACTG Stage here."),
    )

    stage_modifier = models.CharField(
        verbose_name="Overall cancer stage modifier",
        max_length=15,
        null=True,
        blank=True,
        choices=MODIFIER,
        help_text=(
            "For lymphomas, report Ann Arbor Stage here.For Kaposi's, "
            "report 'None'."),
    )

    treatment_itent = models.CharField(
        verbose_name="Treatment intent",
        max_length=15,
        null=True,
        blank=True,
        choices=TREATMENT_INTENT,
    )

    treatment_relationship = models.CharField(
        verbose_name="Relationship to other treatment modalities",
        max_length=55,
        null=True,
        blank=True,
        choices=TREATMENT_RELATIONSHIP,
    )

    side_effects = models.ManyToManyField(
        RadiationSideEffects,
        verbose_name="Side Effects",
        max_length=55,
        blank=True,
        # choices=SIDE_EFFECTS,
        help_text="(tick all that apply)")

    side_effects_other = OtherCharField()

    response = models.CharField(
        verbose_name="Response to Treatment",
        max_length=55,
        null=True,
        blank=True,
        choices=RESPONSE,
    )

    response_other = OtherCharField()

    any_missed_doses = models.CharField(
        verbose_name="Were any doses missed",
        max_length=15,
        null=True,
        blank=True,
        choices=YES_NO_UNKNOWN,
    )

    if_doses_missed = models.CharField(
        verbose_name="If yes, why were treatments missed? ",
        max_length=85,
        null=True,
        blank=True,
        choices=REASONS_MISSED_OR_DELAYED,
    )
    if_doses_missed_other = OtherCharField()
    any_doses_delayed = models.CharField(
        verbose_name="Were any doses delayed",
        max_length=15,
        null=True,
        blank=True,
        choices=YES_NO_UNKNOWN,
    )
    if_doses_delayed = models.CharField(
        verbose_name="If yes, why were treatments delayed? ",
        max_length=85,
        null=True,
        blank=True,
        choices=REASONS_MISSED_OR_DELAYED,
    )

    if_doses_delayed_other = OtherCharField()

    first_course_radiation = models.CharField(
        verbose_name="Was this the first course of radiation",
        max_length=15,
        null=True,
        blank=True,
        choices=YES_NO_UNKNOWN,
    )

    comments = models.CharField(
        verbose_name=("Comments"),
        max_length=250,
        null=True,
        blank=True,
        help_text="",
    )

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Radiation Treatment"


# The radiation table
class BaseRadiationTreatment(BaseUuidModel):

    treatment_name = models.CharField(
        verbose_name="Treatment (eg. Pelvis, Tans, Scar Boost)",
        max_length=50,
        help_text="",
    )
    start_date = models.DateField(
        verbose_name="Start Date",
        max_length=25,
        null=True,
        blank=True,
        help_text="",
    )
    end_date = models.DateField(
        verbose_name="End Date",
        max_length=25,
        null=True,
        blank=True,
        help_text="",
    )
    dose_delivered = models.IntegerField(
        verbose_name="Total Dose Delivered (cGy)",
        blank=True,
        null=True,)
    dose_described = models.IntegerField(
        verbose_name="Total Dose Prescribed (cGy)",
        blank=True,
        null=True,
        max_length=4)
    fractions = models.IntegerField(
        verbose_name="Total Number of Fractions",
        blank=True,
        null=True,
        max_length=3)
    dose_per_fraction = models.IntegerField(
        verbose_name="Dose per Fraction (cGy)",
        blank=True,
        null=True,
        max_length=3)
    radiation_technique = models.CharField(
        verbose_name="Radiation Technique",
        blank=True,
        null=True,
        max_length=25,
        choices=RADIATION_TECHNIQUE,
    )
    radiation_technique_other = OtherCharField()
    modality = models.CharField(
        verbose_name="Modality",
        max_length=25,
        blank=True,
        choices=MODALITY,
    )
    brachy_length = models.CharField(
        verbose_name="Brachy Applicator length (cm)",
        max_length=25,
        null=True,
        blank=True,
        choices=BRACHY_LENGTH,
    )
    brachy_type = models.CharField(
        verbose_name="Brachy Applicator type",
        max_length=25,
        null=True,
        blank=True,
        choices=BRACHY_TYPE,
    )

    class Meta(CrfModelMixin.Meta):
        abstract = True


class RadiationTreatmentRecord(BaseRadiationTreatment):

    radiation_treatment = models.ForeignKey(RadiationTreatment)

#     objects = RadiationTreatmentRecordManager()

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Radiation Treatment Record"
