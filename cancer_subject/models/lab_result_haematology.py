# coding: utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin, \
    CrfModelMixinNonUniqueVisit


class LabResultHaematology(CrfModelMixinNonUniqueVisit):

    haem_drawn_date = models.DateField(
        verbose_name="Date of haematology specimen draw",
        null=True,
        blank=True,
        max_length=25,
        help_text="",
        )

    hgb = models.DecimalField(
        verbose_name="Haemoglobin",
        null=True,
        blank=True,
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(30)],
        help_text="mg/dL",
        )

    mcv = models.DecimalField(
        verbose_name="Mean corpuscular volume (MCV):",
        null=True,
        blank=True,
        max_digits=4,
        decimal_places=1,
        validators=[MinValueValidator(40), MaxValueValidator(150)],
        help_text="microL"
        )

    wbc_count = models.DecimalField(
        verbose_name="White blood cell (WBC) count :",
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(500)],
        help_text="cells/microL"
        )

    anc_count = models.DecimalField(
        verbose_name="Absolute neutrophil count (ANC) :",
        null=True,
        blank=True,
        max_digits=6,
        decimal_places=3,
        validators=[MinValueValidator(0), MaxValueValidator(500)],
        help_text="cells/microL"
        )

    platelet = models.DecimalField(
        verbose_name="Platelet count:",
        null=True,
        blank=True,
        max_digits=5,
        decimal_places=1,
        validators=[MinValueValidator(0), MaxValueValidator(3000)],
        help_text="cells/microL"
        )
    # v2 added comments field for when form has "-3" input
    comments = models.TextField(
        verbose_name="Comments:",
        max_length=100,
        null=True,
        blank=True,
        help_text="if other data not recorded, explain why",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_labresulthaematology_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Lab Result: Haematology"
        verbose_name_plural = "Lab Result: Haematology"
