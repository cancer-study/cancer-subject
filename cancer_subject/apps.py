from datetime import datetime

from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoApponfig
from django.conf import settings
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import MISSED_VISIT
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT


# from edc_sync_files.apps import AppConfig as BaseEdcSyncFilesAppConfig
# from edc_sync.apps import AppConfig as BaseEdcSyncAppConfig
class AppConfig(DjangoApponfig):
    name = 'cancer_subject'
    verbose_name = 'Cancer Subject CRFs'
    admin_site_name = 'cancer_subject_admin'

    screening_age_adult_upper = 99
    screening_age_adult_lower = 18

    def ready(self):
        from .models import subject_screening_on_post_save


if settings.APP_NAME == 'cancer_subject':
    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP045'
        protocol_number = '045'
        protocol_name = 'Cancer'
        protocol_title = ''
        study_open_datetime = datetime(
            2010, 5, 2, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2019, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcLabAppConfig(BaseEdcLabAppConfig):
        base_template_name = 'cancer/base.html'
        requisition_model = 'cancer_subject.subjectrequisition'
        result_model = 'edc_lab.result'

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'cancer_subject': ('subject_visit', 'cancer_subject.subjectvisit')}

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '045'

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'cancer_subject.subjectvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='cancer_subject.appointment',
                related_visit_model='cancer_subject.subjectvisit')
        ]

    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = TimepointCollection(
            timepoints=[
                Timepoint(
                    model='cancer_subject.appointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT),
                Timepoint(
                    model='cancer_subject.historicalappointment',
                    datetime_field='appt_datetime',
                    status_field='appt_status',
                    closed_status=COMPLETE_APPT)
            ])

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}
