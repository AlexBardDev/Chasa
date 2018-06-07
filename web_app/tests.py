from django.test import TestCase
from django.urls import reverse

class ViewsTests(TestCase):
    """This class contains all the tests for the views of this app."""

    def test_home(self):
        """This method tests the 'home' view."""

        response = self.client.get(reverse('home'))

        assert response.status_code == 200

    def test_events(self):
        """This method tests the 'events' view."""

        response = self.client.get(reverse('events'))

        assert response.status_code == 200

    def test_about(self):
        """This method tests the 'about' view."""

        response = self.client.get(reverse('about'))

        assert response.status_code == 200
