# from django.contrib import admin
# from edc_model_admin import audit_fieldset_tuple
#
# from .modeladmin_mixins import CrfModelAdminMixin
#
# from ..admin_site import cancer_subject_admin
# from ..forms import SubjectDeathForm
# from ..models import SubjectDeath, SubjectVisit
# # SubjectDeath
#
#
# @admin.register(SubjectDeath, site=cancer_subject_admin)
# class SubjectDeathAdmin(CrfModelAdminMixin, admin.ModelAdmin):
#
#     form = SubjectDeathForm
#     fieldsets = (
#         (None, {
#             'fields': (
#                 "registered_subject",
#                 "subject_visit",
#                 "death_date",
#                 "is_death_date_estimated",
#                 "death_cause_info",
#                 "death_cause_info_other",
#                 "death_cause",
#                 "death_cause_category",
#                 "death_cause_other",
#                 "comment")}),
#         audit_fieldset_tuple
#     )
# #     list_filter = [
# #         'created',
# #         'user_created',
# #         'hostname_created',
# #         'modified',
# #         'user_modified',
# #         'hostname_modified',
# #         'registered_subject__gender',
# #         'registered_subject__study_site',
# #         'registered_subject__registration_datetime',
# #     ]
# # #     list_display = ('registered_subject', 'subject_visit',
#                             'death_date', 'created', 'user_created',)
# #
# #     def formfield_for_foreignkey(self, db_field, request, **kwargs):
# #         if db_field.name == "subject_visit":
# #             # subject_visit = SubjectVisit.objects.filter(
#                                     id=request.GET.get(db_field.name))
# #             kwargs["queryset"] = SubjectVisit.objects.filter(
# #                 id=request.GET.get(db_field.name, None))
# # return super(SubjectDeathAdmin, self).formfield_for_foreignkey(db_field,
# # request, **kwargs)
