from django.core.management.base import BaseCommand
from django.apps import apps as django_apps
from django.core.exceptions import ValidationError
from django.contrib.sites.models import Site


class SiteModelError(Exception):
    pass


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass
#         parser.add_argument('poll_id', nargs='+', type=int)

    def site_value(self, subject_identifier=None):
        """Return site.
        """
        if subject_identifier[4:6] in ['04', '40']:
            try:
                site = Site.objects.get(id='040')
            except Site.DoesNotExist:
                raise SiteModelError('Site 040 does not exist')
            else:
                return site
        elif subject_identifier[4:6] in ['06', '60']:
            try:
                site = Site.objects.get(id='060')
            except Site.DoesNotExist:
                raise SiteModelError('Site 060 does not exist')
            else:
                return site
        return None


    def handle(self, *args, **options):
        installed_apps = [
            'edc_action_item',
            'edc_reference',
            'edc_registration',
            'edc_visit_schedule',
            'edc_metadata_rules',
            'edc_timepoint',
            'edc_metadata',
            'edc_visit_tracking',
            'edc_facility',
            'cancer_subject',
            'cancer_visit_schedule',
            'cancer_prn'
        ]
        unknown_site = []
        for installed_app in installed_apps:
            app_models = django_apps.get_app_config(installed_app).get_models()
            for app_model in app_models:
                model_fields =  app_model._meta.get_fields()
                model_field_names = []
                for model_field in model_fields:
                    model_field_names.append(model_field.name)
                if 'site' in model_field_names:
                    objs = app_model.objects.all()
                    model_label_lower = app_model._meta.label_lower
                    obj_count = objs.count()
                    self.stdout.write(self.style.WARNING(f'total objects for {model_label_lower}: {obj_count}'))
                    if 'subject_identifier' in model_field_names:
                        for obj in objs:
                            site = self.site_value(subject_identifier=obj.subject_identifier)
                            if site:
                                obj.site=site
                                obj.save_base(raw=True)
                            else:
                                unknown_site.append(obj.subject_identifier)
                        self.stdout.write(self.style.SUCCESS(f'Successfully update site for {model_label_lower}'))
                    elif 'edc_reference.reference' == model_label_lower:
                        for obj in objs:
                            site = self.site_value(subject_identifier=obj.identifier)
                            if site:
                                obj.site=site
                            else:
                                unknown_site.append(obj.identifier)
#                             obj.save_base(raw=True)
                        self.stdout.write(self.style.SUCCESS(f'Successfully update site for {model_label_lower}'))
                    else:
                        for obj in objs:
                            site = self.site_value(subject_identifier=obj.subject_visit.subject_identifier)
                            if site:
                                obj.site=site
                                obj.save_base(raw=True)
                            else:
                                unknown_site.append(obj.subject_visit.subject_identifier)
                        self.stdout.write(self.style.SUCCESS(f'Successfully update site for {model_label_lower}'))
        print('Unknown sites', unknown_site)
