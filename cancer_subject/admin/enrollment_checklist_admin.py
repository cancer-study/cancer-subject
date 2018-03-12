from django.contrib import admin
from django.urls.base import reverse
from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_fieldsets import FieldsetsModelAdminMixin
from edc_model_admin import (
    ModelAdminFormAutoNumberMixin, ModelAdminInstitutionMixin,
    audit_fieldset_tuple, audit_fields, ModelAdminNextUrlRedirectError,
    ModelAdminNextUrlRedirectMixin, ModelAdminReplaceLabelTextMixin)

from ..admin_site import cancer_subject_admin
from ..forms import EnrollmentChecklistForm
from ..models import EnrollmentChecklist


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin, ModelAdminFormAutoNumberMixin,
                      ModelAdminRevisionMixin, ModelAdminReplaceLabelTextMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10
    date_hierarchy = 'modified'
    empty_value_display = '-'

#     def redirect_url(self, request, obj, post_url_continue=None):
#         redirect_url = super().redirect_url(
#             request, obj, post_url_continue=post_url_continue)
#         if request.GET.dict().get('next'):
#             url_name = request.GET.dict().get('next').split(',')[0]
#             attrs = request.GET.dict().get('next').split(',')[1:]
#             options = {k: request.GET.dict().get(k)
#                        for k in attrs if request.GET.dict().get(k)}
#             options.update(subject_identifier=obj.subject_identifier)
#             try:
#                 redirect_url = reverse(url_name, kwargs=options)
#             except NoReverseMatch as e:
#                 raise ModelAdminNextUrlRedirectError(
#                     f'{e}. Got url_name={url_name}, kwargs={options}.')
#         return redirect_url


@admin.register(EnrollmentChecklist, site=cancer_subject_admin)
class EnrollmentChecklistAdmin(ModelAdminMixin, FieldsetsModelAdminMixin,
                               admin.ModelAdmin):

    form = EnrollmentChecklistForm

    fieldsets = (
        (None, {
            'fields': (
                'report_datetime',
                'subject_identifier',
                'has_diagnosis',
                'enrollment_site',
            )}),
        audit_fieldset_tuple)

#     readonly_fields = ('subject_identifier',) + audit_fields
#     readonly_fields = ('subject_identifier',)
    search_fields = ('subject_identifier',)

    radio_fields = {
        'has_diagnosis': admin.VERTICAL,
        'enrollment_site': admin.VERTICAL, }

    def get_readonly_fields(self, request, obj=None):
        return (super().get_readonly_fields(request, obj=obj)
                + audit_fields)

#     def get_form(self, request, obj=None, **kwargs):
#         """Returns a form after adding subject_identifier
#         """
#         form = super().get_form(request, obj=obj, **kwargs)
#         subject_screening = SubjectConsent.objects.get(
#             screening_identifier=request.GET.get('screening_identifier'))
#         if subject_screening.mental_status == ABNORMAL:
#             form = self.replace_label_text(
#                 form, 'participant', 'next of kin', skip_fields=['is_incarcerated'])
#         return form
