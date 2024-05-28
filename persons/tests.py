from django.test import TestCase
from django.urls import reverse

from persons.models import Persons, Position, Skills


class PersonsViewTestCase(TestCase):

    def test_persons_view_post_success(self):
        data = {'first_name': 'Adrian'}
        url = reverse('persons:persons')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)

    def test_persons_view_post_fail(self):
        data = {}
        url = reverse('persons:persons')
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)

    def test_persons_view_get(self):
        url = reverse('persons:persons')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_main_view_get(self):
        url = reverse('persons:main')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_str_persons(self):
        person = Persons(first_name="Imie", last_name="Nazwisko")

        self.assertEqual(str(person), "Imie Nazwisko")

    def test_str_skills(self):
        person = Skills(name="Python")

        self.assertEqual(str(person), "Python")

    def test_str_position(self):
        person = Position(name="Developer")

        self.assertEqual(str(person), "Developer")
