from django.urls import path

from . import views


urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page" ),
    path("posts", views.PostsView.as_view(), name="posts-page"),
    path("posts/<slug>", views.PostDetailView.as_view(), name="post-detail-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later" ),
    path("subscription-page", views.SubscriptionPageView.as_view(), name="subscription-page"),
    path("manage-subscription-page", views.ManageSubscriptionPage.as_view(), name="manage-subscription-page")
]