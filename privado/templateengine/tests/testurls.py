from django.test import SimpleTestCase
from django.urls import resolve,reverse
from templateengine.views import insert_retrive,home



class TestURL(SimpleTestCase):
    def test_home(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_function(self):
        url=reverse('insert_retrive',args=['1234'])
        self.assertEquals(resolve(url).func,insert_retrive)
    