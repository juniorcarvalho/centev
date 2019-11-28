from django.test import TestCase

from crud.core.models import People


class PeopleModelTest(TestCase):
    def setUp(self):
        self.people = People.objects.create(name='Nome', email='email@email.com', telefone='telefone')

    def test_exists(self):
        """test people register"""
        pass

    def test_str(self):
        """ test str """
        self.assertEqual(str(self.people), '{0} - {1}'.format(self.people.name, self.people.email))
