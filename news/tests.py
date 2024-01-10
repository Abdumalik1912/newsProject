from django.test import TestCase
from .models import Posts
from django.urls import reverse

# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Posts.objects.create(title="Men", post="Qalesiz")

    def test_post_model(self):
        post = Posts.objects.get(id=1)
        expected_title = f"{post.title}"
        expected_text = f"{post.post}"
        self.assertEqual(expected_title, "Men")
        self.assertEqual(expected_text, "Qalesiz")


class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Posts.objects.create(title="Men2", post="Qale")

    def test_url_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_url_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")



