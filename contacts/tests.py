
from django.test import TestCase
from django.conf import settings


LANGUAGE_CODE = settings.LANGUAGE_CODE


class ContactTestCase(TestCase):

    def test_index_view(self):

        url = '/{}/contacts/'.format(LANGUAGE_CODE)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)