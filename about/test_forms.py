from django.test import TestCase
from .forms import CollaborateForm


# Create your tests here.

class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test Ickle',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_is_invalid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="name missing but form is valid")

    def test_email_is_invalid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test Ickle',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="email missing but form is valid")

    def test_message_is_invalid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Test Ickle',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(), msg="message missing but form is valid")
