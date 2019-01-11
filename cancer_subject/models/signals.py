from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .subject_consent import SubjectConsent
from .subject_screening import SubjectScreening


@receiver(post_save, weak=False, sender=SubjectScreening,
          dispatch_uid='subject_screening_on_post_save')
def subject_screening_on_post_save(sender, instance, raw, created, **kwargs):
    """Creates an onschedule instance for this enrolled subject, if
    it does not exist.
    """

    if not raw:
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='cancer_subject.onschedule',
                name=instance.schedule_name)
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)
        else:
            # put subject on schedule
            _, schedule = site_visit_schedules.get_by_onschedule_model_schedule_name(
                onschedule_model='cancer_subject.onschedule',
                name=instance.schedule_name)
            schedule.put_on_schedule(
                subject_identifier=instance.subject_identifier,
                onschedule_datetime=instance.report_datetime)

            # Update subject consent with screening identifier
            try:
                subject_consent = SubjectConsent.objects.get(
                    subject_identifier=instance.subject_identifier)
            except SubjectConsent.DoesNotExist:
                raise ValidationError(
                    'Subject Consent for subject '
                    f'{instance.subject_identifier} must exist.')
            else:
                subject_consent.screening_identifier = instance.screening_identifier
                subject_consent.save()
