from django.db import models

from edc.base.model.models import BaseModel

from ..managers import EnrollmentSiteManager


class EnrollmentSite(BaseModel):

    site_name = models.CharField(
        verbose_name="Enrollment Site Name",
        max_length=50,
        help_text="",
        )

    objects = EnrollmentSiteManager()

    def natural_key(self):
        return (self.site_name, )

    def __unicode__(self):
        return self.site_name

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Enrollment Site"
        verbose_name_plural = "Enrollment Site"
