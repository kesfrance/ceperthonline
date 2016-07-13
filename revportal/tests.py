from django.test import TestCase
from revportal.models import Post


# Create your tests here.
class PostTests(TestCase):
    
    def test_str(self):
        post = Post(title="This is a title", synopsis="This is content A")
        
        self.assertEquals(
            str(post.title), "This is a title",
            )
        self.assertEquals(
            str(post.synopsis), "This is content A",
            )