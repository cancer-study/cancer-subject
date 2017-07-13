from edc.subject.off_study.admin import BaseOffStudyModelAdmin


class SubjectOffStudyModelAdmin (BaseOffStudyModelAdmin):

    dashboard_type = 'subject'
    visit_model_name = 'subjectvisit'
