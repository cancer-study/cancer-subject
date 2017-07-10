from django.contrib import admin

from .subject_visit_model_admin import SubjectVisitModelAdmin
from ..models import BaselineHIVHistory, BHHHivTest, BHHWhoIllness, BHHCd4
from ..forms import BaselineHIVHistoryForm, BHHHivTestForm, BHHWhoIllnessForm, BHHCd4Form


# BaselineHIVHistory
class BaselineHIVHistoryAdmin(SubjectVisitModelAdmin):

    form = BaselineHIVHistoryForm
    fields = (
        "subject_visit",
        "has_hiv_result",
        "had_who_illnesses",
        "has_cd4",
        "cd4_result",
        "cd4_drawn_date",
        "has_prior_cd4",
        "nadir_cd4",
        "nadir_cd4_drawn_date",
        "has_vl",
        "vl_result",
        "vl_drawn_date",
        )
    radio_fields = {
        "has_hiv_result": admin.VERTICAL,
        "had_who_illnesses": admin.VERTICAL,
        "has_cd4": admin.VERTICAL,
        "has_prior_cd4": admin.VERTICAL,
        "has_vl": admin.VERTICAL}
admin.site.register(BaselineHIVHistory, BaselineHIVHistoryAdmin)


#BHHHivTest
class BHHHivTestAdmin(SubjectVisitModelAdmin):

    form = BHHHivTestForm
    fields = (
        "subject_visit",
        "hiv_drawn_date",
        "hiv_testdate_est",
        "hiv_result",)
    radio_fields = {
        "hiv_testdate_est": admin.VERTICAL,
        "hiv_result": admin.VERTICAL}
admin.site.register(BHHHivTest, BHHHivTestAdmin)


#BHHWhoIllness
class BHHWhoIllnessAdmin(SubjectVisitModelAdmin):

    form = BHHWhoIllnessForm
    fields = (
        "subject_visit",
        "who_illness_date",
        "who_illness",
        "who_illness_other",)
    filter_horizontal = (
        "who_illness",)
admin.site.register(BHHWhoIllness, BHHWhoIllnessAdmin)


#BHHCd4
class BHHCd4Admin(SubjectVisitModelAdmin):

    form = BHHCd4Form
    fields = (
        "subject_visit",
        "nadir_cd4",
        "nadir_cd4_drawn_date")
admin.site.register(BHHCd4, BHHCd4Admin)
