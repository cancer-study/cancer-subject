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
