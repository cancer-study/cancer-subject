from django.test import TestCase, tag

from edc_reference.site import site_reference_configs


@tag('1')
class TestReference(TestCase):

    def test_(self):
        site_reference_configs.validate()
