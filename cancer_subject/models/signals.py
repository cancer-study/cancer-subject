# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from .subject_visit import SubjectVisit


# @receiver(post_save, weak=False,
#           dispatch_uid='remove_other_meta_data_on_post_save')
# def remove_other_meta_data_on_post_save(
#         sender, instance, raw, created, using, **kwarg):
#     if isinstance(instance, SubjectVisit):
#         instance.remove_other_meta_data_on_post_save()


# @receiver(post_save, weak=False,
#           dispatch_uid='create_scheduled_entry_at_7000_offstudy')
# def create_scheduled_entry_at_7000_offstudy(
#         sender, instance, raw, created, using, **kwarg):
#     if isinstance(instance, SubjectVisit):
#         instance.create_scheduled_entry_at_7000_offstudy()
from django.db.models.signals import post_save
from django.dispatch import receiver
from edc_visit_schedule.site_visit_schedules import site_visit_schedules

from .enrollment_checklist import EnrollmentChecklist


@receiver(post_save, weak=False, sender=EnrollmentChecklist,
          dispatch_uid='enrollment_checklist_on_post_save')
def enrollment_checklist_on_post_save(sender, instance, raw, created,
                                      **kwargs):
    """Creates an onschedule instance for this enrolled subject, if
    it does not exist.
    """

    if not raw:
        if not created:
            _, schedule = site_visit_schedules.get_by_onschedule_model(
                'cancer_subject.onschedule')
            schedule.refresh_schedule(
                subject_identifier=instance.subject_identifier)

    # put subject on schedule
    _, schedule = site_visit_schedules.get_by_onschedule_model(
        'cancer_subject.onschedule')
    schedule.put_on_schedule(
        subject_identifier=instance.subject_identifier,
        onschedule_datetime=instance.report_datetime)
