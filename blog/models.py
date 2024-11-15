from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption



class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()
    


# models.py





class StaticImage(models.Model):
    name = models.CharField(max_length=255)  # A name for the image
    filename = models.CharField(max_length=255)  # Store the relative path to the image in the static folder

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ForeignKey(StaticImage, null=True, blank=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title
       




class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")


class Subscription(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.email
    
    def get_subscriber_info(self):
    
        return {
            "id" : self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name
        }




    
    

