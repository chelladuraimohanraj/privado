from django.test import TestCase,Client
from django.urls import reverse

class TestViews(TestCase):
    def test_insert_retrive_GET(self):
        client=Client()

        response=client.get(reverse('insert_retrive',args=['1234']))

        self.assertEqual(response.status_code,200)
    def test_insert_retrive_POST(self):
        client=Client()

        response=client.post(reverse('insert_retrive',args=['1234']))

        self.assertEqual(response.status_code,200)


