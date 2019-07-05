from django.core.management.base import BaseCommand
from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_action_item.site_action_items import site_action_items

from ...models import SubjectScreening

SUBJECT_LOCATOR_ACTION = 'submit-subject-locator'


class SubjectLocatorViewMixinError(Exception):
    pass


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass
#         parser.add_argument('poll_id', nargs='+', type=int)

    def get_subject_locator_or_message(self, subject_identifier=None):
        model_cls = django_apps.get_model('cancer_subject.subjectlocator')
        try:
            model_cls.objects.get(
                subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            action_cls = site_action_items.get(model_cls.action_name)
            action_item_model_cls = action_cls.action_item_model_cls()
            try:
                action_item_model_cls.objects.get(
                    subject_identifier=subject_identifier,
                    action_type__name=SUBJECT_LOCATOR_ACTION)
            except ObjectDoesNotExist:
                action_cls(
                    subject_identifier=subject_identifier)

    def handle(self, *args, **options):
        
        subject_eligibility = SubjectScreening.objects.filter(eligible=True)
        total = subject_eligibility.count()
        count = 0
        for eligibility in subject_eligibility:
            subject_identifier = eligibility.subject_identifier
            self.get_subject_locator_or_message(subject_identifier=subject_identifier)
            count += 1
            self.stdout.write(self.style.SUCCESS(f'Successfully created locator action items {count} out of {total}'))
        self.stdout.write(self.style.SUCCESS('Successfully created locator action items'))