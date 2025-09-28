from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


# Create your tests here.
class CollabFormTest(TestCase):
    def setUp(self):
        """Creates about_me mock content"""
        self.about = About(
            title='About Me',
            content='A little bit of text',
        )
        self.about.save()

    def test_collaborate_form_exists(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse('about'))
        # Lines to print out classes and id's for debugging - left here for future reference
        # print(response.context['collaborate_form'].__class__)
        # print(id(response.context['collaborate_form'].__class__))
        # print(CollaborateForm.__class__)
        # print(id(CollaborateForm))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_collaboration_form(self):
        """Tests POST of collaboration form"""
        post_data = {
            'name': "Michael Caine",
            'email': "doors@missingparts.co.uk",
            'message': "BOOM!"
        }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Collaboration request received!", response.content)
