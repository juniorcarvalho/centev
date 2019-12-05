from django.test import TestCase

from crud.core.forms import PeopleForm


class HomeViewGetTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """get '/' return status code 200"""
        self.assertEqual(200, self.response.status_code)

    def test_use_template(self):
        """está usando core/template/index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_html(self):
        """Html contém input tags"""
        self.assertContains(self.response, '<form')
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 2)
        self.assertContains(self.response, 'type="email"', 1)
        self.assertContains(self.response, 'type="submit"', 1)

    def test_csrf(self):
        """html contém csrf"""
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_has_form(self):
        """context contem PeopleForm"""
        form = self.response.context['form']
        self.assertIsInstance(form, PeopleForm)

    def test_form_has_fields(self):
        """form contém os campos"""
        form = self.response.context['form']
        self.assertSequenceEqual(['name', 'email', 'telefone'], list(form.fields))
