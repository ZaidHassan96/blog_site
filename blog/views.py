from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.views.generic import ListView, FormView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings

from .models import Post, Subscription
from .forms import CommentForm, SubscriptionForm
from django.contrib import messages
from django.core.mail import send_mail




def get_date(post):
    return post['date']
    



class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the stored subscribers from the session
        stored_subscriber = self.request.session.get("stored_subscriber")
        
        # Determine if the user has subscribed
        # Assuming `subscription_id` is obtained from somewhere; replace with actual ID if needed
        
        print(stored_subscriber)
      
        # Add subscription status to the context
        context["user_subscribed"] = stored_subscriber
        context["page_style"] = "style-one"
     

        return context
        
    
    # def post(self, request):
    #     subscription_form = SubscriptionForm(request.POST)
    #     if subscription_form.is_valid():
    #         subscription_form.save()
    #         return HttpResponseRedirect(reverse("starting-page"))
        
    #     context = {
    #         "posts" : self.get_queryset(),
    #         "subscription_form": subscription_form


    #     }

    #     return render(request, "blog/index.html", context)





# def starting_page(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]
 
#     return render(request,"blog/index.html", {"posts": latest_posts})

class PostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve the stored subscribers from the session
        stored_subscriber = self.request.session.get("stored_subscriber")
        
        # Determine if the user has subscribed
        # Assuming `subscription_id` is obtained from somewhere; replace with actual ID if needed
        
        print(stored_subscriber)
      
        # Add subscription status to the context
        context["user_subscribed"] = stored_subscriber

        return context

   


class PostDetailView(View):
    template_name = "blog/post-detail.html"
    model = Post




    

    def is_stored_post(self, request, post_id):
        stored_posts =  request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later


    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        stored_subscriber = self.request.session.get("stored_subscriber")

 
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id),
            "user_subscribed": stored_subscriber
        }

        

   
        return render(request, "blog/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
           comment = comment_form.save(commit=False)
           comment.post = post
           comment.save()
           return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)
    


class ReadLaterView(View):



    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        stored_subscriber = self.request.session.get("stored_subscriber")


        context = {
            "user_subscribed": stored_subscriber,
            "has_posts": bool(stored_posts)
        }

    
        
        
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True
        
        return render(request, "blog/stored-posts.html", context )
    
    

            


    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
            
        post_id = int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts
            


        return HttpResponseRedirect("/")
        
        
class SubscriptionPageView(FormView):
    template_name = "blog/subscription-page.html"
    form_class = SubscriptionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stored_subscriber = self.request.session.get("stored_subscriber")
        context["user_subscribed"] = stored_subscriber
        context["subscription_form"] = self.get_form()
        return context
    
    def form_valid(self, form):
        subscription = form.save()
        subscriber_info = subscription.get_subscriber_info()
        stored_subscriber = self.request.session.get("stored_subscriber", False)
        if not stored_subscriber:
             self.request.session["stored_subscriber"] = True
        
       
       

        print(subscription)  # Save the form
        print(subscriber_info)
        self.send_subscription_email(subscriber_info)  # Send the email
        return HttpResponseRedirect(reverse("starting-page"))

    def form_invalid(self, form):
        context = self.get_context_data(subscription_form=form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def send_subscription_email(self, subscriber_info):
        
        subject = 'Thank you for subscribing!'
        message = f'Dear {subscriber_info["first_name"]},\n\nThank you for subscribing to our newsletter!'
        from_email = settings.DEFAULT_FROM_EMAIL 
        recipient_list = [subscriber_info["email"]]  # Send to the subscriber's email

        send_mail(subject, message, from_email, recipient_list)
    
class ManageSubscriptionPage(FormView):
    template_name = "blog/manage-subscription-page.html"
    form_class = SubscriptionForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stored_subscriber = self.request.session.get("stored_subscriber")

        context['email_not_found'] = False
        context["user_subscribed"] = stored_subscriber
          # Initialize as False
        return context

    def post(self, request, *args, **kwargs):
        email = request.POST.get('subscription_email')
        context = self.get_context_data()
        print(email)
          
        if email:
            try:
                subscription = Subscription.objects.get(email=email)
                print(subscription, "hello")
                subscription.delete()
                stored_subscriber = self.request.session.get("stored_subscriber", False)
                if stored_subscriber:
                    self.request.session["stored_subscriber"] = False

            
            except Subscription.DoesNotExist:
                context['email_not_found'] = True
                return render(request, "blog/manage-subscription-page.html", context)
                
                # Handle the case where the email is not found
                
        return HttpResponseRedirect(reverse("starting-page"))

          




        





    # def get_context_data(self, **kwargs: Any):
    #     context =  super().get_context_data(**kwargs)
    #     context["post_tags"] = self.object.tags.all()
    #     context["comment_form"] = CommentForm()
    #     return context
    
# def post_detail(request, slug):
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {"post": identified_post,
#      "post_tags":identified_post.tags.all()})


