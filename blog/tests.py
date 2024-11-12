from django.test import TestCase
from .models import Post, Author, Tag, Comment
from django.utils.text import slugify
from django.core.exceptions import ValidationError  # Import ValidationError



class TagModelTestCase(TestCase):
     def setUp(self):
          self.tag = Tag.objects.create(caption="TestTag")
    
     def test_tag_creation(self):
          self.assertEqual(self.tag.caption, "TestTag")
     
     def test_tag_str(self):
          self.assertEqual(str(self.tag), "TestTag")

     def test_max_length_tag(self):
          long_tag = Tag(caption="a" * 30)
          with self.assertRaises(ValidationError):
               long_tag.full_clean()
     
     
          
          


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
        
    
    def test_title_max_length(self):
        """Test that the title does not exceed the max_length of 100 characters."""
        long_title = "x" * 101  # Create a title that exceeds 100 characters
        post_with_long_title = Post(
            title=long_title,
            excerpt="Test Excerpt",
            content="This is a test content with more than ten characters.",
            author=self.author,
            slug=slugify("Test Long Title")
        )

        with self.assertRaises(ValidationError):
             post_with_long_title.full_clean()


class CommentModelTestCase(TestCase):
    def setUp(self):
          
          author = Author.objects.create(
               first_name="John",
               last_name="Jones",
               email_address="johnj@hotmail.com"
          )

          post = Post.objects.create(
            title="The adventures of John",
            excerpt="John and his adventures",
            content="John has been on many different adventures all across the globe..",
            author=author
          )
          self.comment = Comment.objects.create(
               user_name="Zaid",
               user_email="zaid@hotmail.com",
               text="Amazing post!",
               post=post


          )

    def test_comment_creation(self):
         self.assertTrue(isinstance(self.comment, Comment ))
         self.assertEqual(self.comment.user_name, "Zaid")
         self.assertEqual(self.comment.user_email, "zaid@hotmail.com")
         self.assertEqual(self.comment.text, "Amazing post!")
         
         
     

     




