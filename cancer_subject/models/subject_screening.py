from django.db import models
from edc_base.model_managers import HistoricalRecords
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import eligible_if_yes
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_base.utils import get_utcnow
from edc_constants.choices import YES_NO
from edc_identifier.model_mixins import UniqueSubjectIdentifierFieldMixin
from edc_search.model_mixins import SearchSlugManager

from ..eligibility import Eligibility
from ..models.model_mixins import SearchSlugModelMixin
from ..screening_identifier import ScreeningIdentifier


ENROLLMENT_SITES = (
    ('gaborone_private_hospital', ' Gaborone Private Hospital (GPH)'),
    ('nyangabgwe_referral_Hospital', 'Nyangabgwe Referral Hospital (NRH)'),
    ('princess_marina_hospital', 'Princess Marina Hospital (PMH)'),
    ('bokamoso_private_hospital', 'Bokamoso Private Hospital (BPH)'),
)


class EnrollmentManager(SearchSlugManager, models.Manager):

    def get_by_natural_key(self, screening_identifier):
        return self.get(
            screening_identifier=screening_identifier
        )


class SubjectScreening(
        UniqueSubjectIdentifierFieldMixin, SiteModelMixin,
        SearchSlugModelMixin, BaseUuidModel):

    eligibility_cls = Eligibility
    identifier_cls = ScreeningIdentifier

    screening_identifier = models.CharField(
        verbose_name="Eligibility Identifier",
        max_length=36,
        unique=True,
        editable=False)

    report_datetime = models.DateTimeField(
        verbose_name='Report Date and Time',
        default=get_utcnow,
        help_text='Date and time of report.')

    has_diagnosis = models.CharField(
        verbose_name="Has a cancer diagnosis been documented? ",
        max_length=3,
        choices=YES_NO,
        validators=[eligible_if_yes, ],
        help_text="( if 'NO' STOP patient cannot be enrolled )",)

    enrollment_site = models.CharField(
        max_length=100,
        null=True,
        choices=ENROLLMENT_SITES,
        help_text="Hospital where subject is recruited")

    eligible = models.BooleanField(
        default=False,
        editable=False)

    objects = EnrollmentManager()

    def __str__(self):
        return f'{self.screening_identifier}, {self.subject_identifier}'

    def natural_key(self):
        return (self.subject_identifier,)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        eligibility_obj = self.eligibility_cls(
            cancer_status=self.has_diagnosis)
        self.eligible = eligibility_obj.eligible
        if not self.id:
            self.screening_identifier = self.identifier_cls().identifier
        super().save(*args, **kwargs)

    @property
    def schedule_name(self):
        """Return a visit schedule name.
        """
        return 'schedule'

    class Meta:
        app_label = 'cancer_subject'
        verbose_name = "Cancer Eligibility"
        verbose_name_plural = "Cancer Eligibility"
