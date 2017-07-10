from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.choices.common import YES_NO

from .base_scheduled_visit_model import BaseScheduledVisitModel
from ..choices.baseline_hiv_history import RECENT_RESULT_CHOICE


class BHHHivTest (BaseScheduledVisitModel):

    hiv_drawn_date = models.DateField(
        verbose_name="Date of most recent HIV test:",
        max_length=25,
        help_text="",
        )
    #v2 added field for when exact date is unknown
    hiv_testdate_est = models.CharField(
        verbose_name="Is the HIV test date estimated?",
        max_length=3,
        choices=YES_NO,
        help_text="",
        )
    hiv_result = models.CharField(
        verbose_name=("Result of most recent HIV test:"),
        max_length=50,
        choices=RECENT_RESULT_CHOICE,
        help_text=("If last HIV test negative (or Don't Know) and more "
                     "than six months ago, perform HIV testing unless "
                     "patient refuses."),
        )

    history = AuditTrail()

    def get_visit(self):
        return self.hiv_drawn_date

    def get_result_datetime(self):
        return self.registration_datetime

#     def get_test_code(self):
#         return 'HIV'
#
#     def get_result_value(self, attr=None):
#         """Returns a result value for given attr name for the lab_tracker."""
#         retval = None
#         if not attr in dir(self):
#             raise TypeError('Attribute {0} does not exist in model {1}'.format(attr, self._meta.object_name))
#         if attr == 'hiv_result':
#             if self.hiv_result.lower() == 'pos':
#                 retval = 'POS'
#             elif self.hiv_result.lower() == 'neg':
#                 retval = 'NEG'
#             else:
#                 retval = 'UNK'
#         return retval

    def __unicode__(self):
        return unicode(self.subject_visit)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_bhhhivtest_change', args=(self.id,))

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "BHH: HIV Test"
