from django import forms

from .models import Comment, Subscription

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }



class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email', 'first_name', 'last_name']
        labels = {
            "email": "Email",
            "first_name": "Forename",
            "last_name": "Surname"

        }

