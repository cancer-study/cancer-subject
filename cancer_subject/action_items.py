from edc_locator.action_items import SubjectLocatorAction as BaseSubjectLocatorAction

from edc_action_item import site_action_items


SUBJECT_LOCATOR_ACTION = 'submit-cancer-subject-locator'


class CancerSubjectLocatorAction(BaseSubjectLocatorAction):
    name = SUBJECT_LOCATOR_ACTION
    display_name = 'Submit Subject Locator'
    reference_model = 'cancer_subject.subjectlocator'
    admin_site_name = 'cancer_subject_admin'


site_action_items.register(CancerSubjectLocatorAction)
