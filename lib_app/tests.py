from django.test import TestCase

from django.urls import reverse

from .models import Book


class TestPageTests(TestCase):
    def test_test_page_displays_books(self):
        Book.objects.create(
            title="Django for Beginners",
            category="Programming",
            description="Learn Django fundamentals.",
            price="25.00",
        )

        response = self.client.get(reverse("test"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lib_app/test.html")
        self.assertContains(response, "Django for Beginners")
        self.assertContains(response, "Programming")
        self.assertContains(response, "Learn Django fundamentals.")
        self.assertContains(response, "25.00")
