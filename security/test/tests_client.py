from django.test import TestCase
from django.urls import reverse

from security.models import Client


class ClientTest(TestCase):
    def setUp(self):
        self.user = Client.objects.create(
            username="test_user_login",
            email="",
            first_name="Doe",
            last_name="John",
            password="password",
        )

        self.client1 = Client.objects.create_user(
            username="test_client1",
            last_name="",
            first_name="",
            email="",
            password="password",
        )

        self.client2 = Client.objects.create_user(
            username="test_client2",
            last_name="Bill",
            first_name="Watson",
            email="",
            password="password",
        )

    def test_create_user(self):
        self.client.force_login(self.user)

        url = reverse("security:client-list")
        response = self.client.get(url, {"username": "test_client1"})

        self.assertContains(response, self.client1.username)
        self.assertNotContains(response, self.client2.username)

        self.assertEqual(response.status_code, 200)

    def test_search_client(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("security:client-list"),
            {"username": ""},
        )

        self.assertContains(response, self.client1.username)


    def test_search_no_results_client(self):
        self.client.force_login(self.user)

        response = self.client.get(
            reverse("security:client-list"),
            {"username": "NonExistent"},
        )

        self.assertEqual(len(response.context["client_list"]), 0)
