from django.test import TestCase
from .models import Profile, Image, Comment, Follow

# Create your tests here.
class FollowTestClass(TestCase):
    def setUp(self):
        self.moringa=Follow(username='moringa',followed='kibocha')
                            
    def test_instance(self):
        self.assertTrue(isinstance(self.moringa,Follow))

class CommentTestClass(TestCase):
    def setUp(self):
        self.first=Comment(post=1,
                            username='moringa',
                            comment='Love it.',
                            date='Apr 2, 2022, 20:22 p.m.',
                            count=0)

    def test_instance(self):
        self.assertTrue(isinstance(self.first,Comment))

