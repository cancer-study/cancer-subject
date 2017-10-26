from django.test import TestCase, tag

from model_mommy import mommy

from ..screening_identifier import ScreeningIdentifier
from ..models import IdentifierHistory


class TestIdentifiers(TestCase):

    def test_identifier(self):
        identifier = ScreeningIdentifier()
        self.assertTrue(identifier.identifier)
        self.assertTrue(identifier.identifier.startswith('S'))

    def test_identifier_history(self):
        identifier = ScreeningIdentifier()
        try:
            IdentifierHistory.objects.get(identifier=identifier.identifier)
        except IdentifierHistory.DoesNotExist:
            self.fail('IdentifierHistory.DoesNotExist unexpectedly raised')

    def test_model_allocates_identifier(self):
        obj = mommy.make_recipe('ambition_subject.subjectscreening')
        self.assertIsNotNone(obj.screening_identifier)
        self.assertTrue(obj.screening_identifier.startswith('S'))
