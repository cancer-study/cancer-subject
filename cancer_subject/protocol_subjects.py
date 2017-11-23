from edc_protocol.subject_type import SubjectType

from edc_protocol.constants import ALL_SITES
from edc_protocol.site_protocol_subjects import site_protocol_subjects


subject = SubjectType(
    name='subject',
    verbose_name='Research Subjects',
    model='cancer_subject.subjectconsent')

subject.add_enrollment_cap(study_site=ALL_SITES, max_subjects=1000)

site_protocol_subjects.register(subject)
