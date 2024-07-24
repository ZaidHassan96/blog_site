from django.test import TestCase
from .models import Post, Author, Tag, Comment
from django.utils.text import slugify
from django.core.exceptions import ValidationError  # Import ValidationError


class PostModelTestCase(TestCase):
    
    def setUp(self):
        self.tag = Tag.objects.create(caption="TestTag")
        self.author = Author.objects.create(first_name = "max", last_name = "davis", email_address = "max1@hotmail.com")
        self.post = Post.objects.create(
            title="Test Title",
            excerpt="Test Excerpt",
            content="This is a test content with more than ten characters.",
            author=self.author
        )
        self.post.tags.add(self.tag)

    def test_excerpt_length(self):
         post = Post(title='Valid Title', excerpt='x' * 201, image = "hello", slug = slugify("Valid Title"), content='Valid content', author=self.author)
         with self.assertRaises(ValidationError):
              post.full_clean()
    
    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post  ))
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_min_length_validator(self):
       
            post_with_short_content= Post.objects.create(
                title="Another Title",
                excerpt="Another Excerpt",
                content="Too",
                author=self.author,
                slug=slugify("Another Title")
            )

            with self.assertRaises(ValidationError) as cm:
                 post_with_short_content.full_clean()  
        
            self.assertIn('content', cm.exception.message_dict)
        





