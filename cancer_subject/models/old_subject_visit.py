from django.db import models
from django.core.urlresolvers import reverse

from edc.audit.audit_trail import AuditTrail
from edc.subject.visit_tracking.models.base_visit_tracking import BaseVisitTracking
from edc.subject.visit_tracking.settings import VISIT_REASON_NO_FOLLOW_UP_CHOICES
from edc.subject.entry.models import Entry
from edc.entry_meta_data.models import ScheduledEntryMetaData

from ..choices import VISIT_UNSCHEDULED_REASON, VISIT_REASON
from subject_off_study_mixin import SubjectOffStudyMixin


class SubjectVisit(SubjectOffStudyMixin, BaseVisitTracking):

    reason_unscheduled = models.CharField(
        verbose_name="If 'Unscheduled' above, provide reason for the unscheduled visit",
        max_length=25,
        blank=True,
        null=True,
        choices=VISIT_UNSCHEDULED_REASON,
        )

    history = AuditTrail()

    @property
    def registered_subject(self):
        return self.get_registered_subject()

    def __unicode__(self):
        return unicode(self.appointment)

    def get_absolute_url(self):
        return reverse('admin:cancer_subject_subjectvisit_change', args=(self.id,))

    def get_visit_reason_choices(self):
        return VISIT_REASON

    def get_visit_reason_no_follow_up_choices(self):
        dct = {'Missed quarterly visit': 'Missed quarterly visit',
                'lost': 'Lost to follow-up',
                'death': 'Death',
                'deferred': 'Deferred'}
        for item in VISIT_REASON_NO_FOLLOW_UP_CHOICES:
            dct.update({item: item})
        del dct['death']
        return dct

    def get_visit_reason_follow_up_choices(self):
        return {'scheduled': 'Quarterly visit/contact',
                'unscheduled': 'Unscheduled visit/contact',
                'off study': 'Off Study'}

    def save(self, *args, **kwargs):
        if self.appointment.visit_definition.code != '1000':
            self.appointment.appt_type = 'telephone'
        #setting default for last visit to be an off study
        if self.appointment.visit_definition.code == '7000':
            self.reason = 'off study'
        self.create_meta_data_when_visit_reason_is_death()
        self.create_meta_data_when_visit_reason_is_off_study()
        self.create_meta_data_only_if_subject_is_female()
        super(SubjectVisit, self).save(*args, **kwargs)

    def remove_other_meta_data_on_post_save(self):
        if self.reason == 'Death':
            required_forms = ['subjectdeath', 'subjectoffstudy']
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
            for meta_data in scheduled_meta_data:
                if meta_data.entry.model_name not in required_forms:
                    meta_data.delete()
        elif self.reason == 'off study':
            required_forms = ['subjectoffstudy']
            scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, registered_subject=self.registered_subject)
            for meta_data in scheduled_meta_data:
                if meta_data.entry.model_name not in required_forms:
                    meta_data.delete()

    def create_meta_data_when_visit_reason_is_death(self):
        if self.reason == 'Death':
            forms = ['subjectdeath', 'subjectoffstudy']
            for form in forms:
                entry = Entry.objects.filter(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                if entry:
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    def create_meta_data_when_visit_reason_is_off_study(self):
        if self.reason == 'off study' or self.reason == 'Lost to follow-up':
            entry = Entry.objects.filter(model_name='subjectoffstudy', visit_definition_id=self.appointment.visit_definition_id)
            if entry:
                scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                if not scheduled_meta_data:
                    scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                else:
                    scheduled_meta_data = scheduled_meta_data[0]
                scheduled_meta_data.entry_status = 'NEW'
                scheduled_meta_data.save()

    def create_scheduled_entry_at_7000_offstudy(self):
        if self.appointment.visit_definition.code == '7000':
            if self.reason == 'off study':
                forms = ['activityandfunctioning', 'currentsymptoms']
                for form in forms:
                    entry = Entry.objects.filter(model_name=form, visit_definition_id=self.appointment.visit_definition_id)
                    if entry:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                        if not scheduled_meta_data:
                            scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                        else:
                            scheduled_meta_data = scheduled_meta_data[0]
                        scheduled_meta_data.entry_status = 'NEW'
                        scheduled_meta_data.save()

    def create_meta_data_only_if_subject_is_female(self):
        if self.appointment.visit_definition.code == '1000':
            from edc.subject.registration.models import RegisteredSubject
            rs = RegisteredSubject.objects.filter(gender='F')
            if rs:
                entry = Entry.objects.filter(model_name='baseriskassessmentfemale', visit_definition_id=self.appointment.visit_definition_id)
                if entry:
                    scheduled_meta_data = ScheduledEntryMetaData.objects.filter(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                    if not scheduled_meta_data:
                        scheduled_meta_data = ScheduledEntryMetaData.objects.create(appointment=self.appointment, entry=entry[0], registered_subject=self.registered_subject)
                    else:
                        scheduled_meta_data = scheduled_meta_data[0]
                    scheduled_meta_data.entry_status = 'NEW'
                    scheduled_meta_data.save()

    class Meta:
        app_label = "cancer_subject"
        verbose_name = "Subject Visit"
