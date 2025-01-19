from http import HTTPStatus

from django.test import TestCase
from django.core.management import call_command
from django.urls import reverse


class RiddleTestCase(TestCase):

    def test_riddle_status_code(self):
        
        response = self.client.get(reverse("riddle-view"))
        
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_home_page_view(self):

        response = self.client.get(reverse("home-view"))

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_custom_management_command(self):
        
        call_command("get_riddles_data")