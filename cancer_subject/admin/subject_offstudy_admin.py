# from django.contrib import admin
# from edc_base.modeladmin_mixins import audit_fieldset_tuple
#
# from ..admin_site import cancer_subject_admin
# from ..forms import SubjectOffStudyForm
# from ..models import SubjectOffstudy
# from .modeladmin_mixins import ModelAdminMixin
#
#
# @admin.register(SubjectOffstudy, site=cancer_subject_admin)
# class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):
#
#     form = SubjectOffStudyForm
#
#     fieldsets = (
#         (None, {
#             'fields': (
#                 'subject_identifier',
#                 'offstudy_datetime',
#                 'reason',
#                 'reason_other',
#                 'comment')}),
#         audit_fieldset_tuple,
#     )
