from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post,Rating

# Create your tests here.
class ProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='mary',email="mary@gmail.com", password='password')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class PostTest(TestCase):

       def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

