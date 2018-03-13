from datetime import datetime
import os

from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoApponfig
from django.conf import settings
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_base.utils import get_utcnow
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
# from edc_sync_files.apps import AppConfig as BaseEdcSyncFilesAppConfig

from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_base_test.apps import AppConfig as BaseEdcBaseTestAppConfig
from edc_consent.apps import AppConfig as BaseEdcConsentAppConfig
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
# from edc_sync.apps import AppConfig as BaseEdcSyncAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import MISSED_VISIT
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT


class AppConfig(DjangoApponfig):
    name = 'cancer_subject'
    admin_site_name = 'cancer_subject_admin'

    screening_age_adult_upper = 99
    screening_age_adult_lower = 18

    def ready(self):
        from .models.signals import enrollment_checklist_on_post_save

        # if 'migrate' not in sys.argv and 'makemigrations' not in sys.argv:
        #    load_randomization()


if settings.APP_NAME == 'cancer_subject':
    class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
        protocol = 'BHP045'
        protocol_number = '045'
        protocol_name = 'Cancer'
        protocol_title = ''
        study_open_datetime = datetime(
            2016, 12, 31, 0, 0, 0, tzinfo=gettz('UTC'))
        study_close_datetime = datetime(
            2018, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))

    class EdcLabAppConfig(BaseEdcLabAppConfig):
        base_template_name = 'cancer/base.html'
        requisition_model = 'cancer_subject.subjectrequisition'
        result_model = 'edc_lab.result'

    class EdcBaseAppConfig(BaseEdcBaseAppConfig):
        project_name = 'cancer'
        institution = 'Botswana-Harvard AIDS Institute'
        copyright = '2017-{}'.format(get_utcnow().year)
        license = None

    class EdcBaseTestAppConfig(BaseEdcBaseTestAppConfig):
        consent_model = 'cancer_subject.subjectconsent'

    class EdcConsentAppConfig(BaseEdcConsentAppConfig):
        pass

    class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
        device_role = CENTRAL_SERVER
        device_id = '99'

    class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
        visit_models = {
            'cancer_subject': ('subject_visit', 'cancer_subject.subjectvisit')}

    class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
        identifier_prefix = '092'

    class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):
        reason_field = {'cancer_subject.subjectvisit': 'reason'}
        create_on_reasons = [SCHEDULED, UNSCHEDULED]
        delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY, MISSED_VISIT]

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        app_label = 'cancer_subject'
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='cancer_subject.subjectvisit')
        ]

    class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
        country = 'botswana'
        definitions = {
            '7-day clinic': dict(days=[MO, TU, WE, TH, FR, SA, SU],
                                 slots=[100, 100, 100, 100, 100, 100, 100]),
            '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                                 slots=[100, 100, 100, 100, 100])}

    class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):
        timepoints = [
            Timepoint(
                model='edc_appointment.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status='DONE'
            ),
            Timepoint(
                model='cancer_subject.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status='DONE'
            ),
        ]

#     class EdcSyncAppConfig(BaseEdcSyncAppConfig):
#         edc_sync_files_using = True
#         role = CENTRAL_SERVER
#
#     class EdcSyncFilesAppConfig(BaseEdcSyncFilesAppConfig):
#         edc_sync_files_using = True
#         role = CENTRAL_SERVER
