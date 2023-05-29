from django.apps import apps as django_apps
from django.core.exceptions import ValidationError


class ConsentVersionModelMixin:
    def get_consent_version(self):
        subject_consent_cls = django_apps.get_model(
            'cancer_subject.subjectconsent')
        try:
            subject_consent_obj = subject_consent_cls.objects.get(
                subject_identifier=self.visit.subject_identifier)
        except subject_consent_cls.DoesNotExist:
            raise ValidationError(
                'Subject {} is Missing Consent obj'.format(
                    self.visit.subject_identifier))
        else:
            return subject_consent_obj.version

    def save(self, *args, **kwargs):
        self.consent_version = self.get_consent_version()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
