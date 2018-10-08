# from datetime import datetime
# from django.db import models
#
# from edc.base.model.validators import ( datetime_not_before_study_start,
#                                         datetime_not_future)
# from edc.entry_meta_data.managers import EntryMetaDataManager
#
# from subject_visit import SubjectVisit
# from subject_base_uuid_model import SubjectBaseUuidModel
# from .model_mixins.crf_model_mixin import CrfModelMixin
#
#
# class BaseScheduledVisitModel(CrfModelMixin):
#
#     """ Base model for all scheduled models
#         (adds key to :class:`SubjectVisit`). """
#
#     report_datetime = models.DateTimeField("Today's date",
#         validators=[
#             datetime_not_before_study_start,
#             datetime_not_future, ],
#         default=datetime.today(),)
#
#     class Meta:
#         abstract = True
