from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.base.model.fields.custom.custom_fields import OtherCharField

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ...cancer_list.models import WhoIllness
from cancer_subject.models.model_mixins.crf_model_mixin import CrfModelMixin


class BHHWhoIllness (CrfModelMixin):

    who_illness = models.ManyToManyField(WhoIllness,
        verbose_name="What WHO stage 3 or 4 illnesses the patient had:",
        max_length=35,
        null=True,
        help_text=("Tick all that apply.  DO NOT include current cancer diagnosis"),
        )

    who_illness_other = OtherCharField()

    who_illness_date = models.DateField(
        verbose_name="Date of most recent WHO stage 3 or 4 illness:",
        max_length=25,
        null=True,
        blank=True,
        help_text="DO NOT include the current cancer diagnosis.",
        )

    history = AuditTrail()

    def get_visit(self):
        return self.subject_visit

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_bhhwhoillness_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "BHH: WHO illness"
        verbose_name_plural = "BHH: WHO illness"
