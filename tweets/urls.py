from django.urls import path
from django.views.generic import RedirectView

from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView,
    TweetUpdateView,
    TweetDeleteView,
)

urlpatterns=[
    path('',RedirectView.as_view(url='/')), #/redirect/

    path('search/',TweetListView.as_view(),name="list"), #/tweet/

    path('create/',TweetCreateView.as_view(),name="create"),#/tweet/create
    path('<int:pk>/',TweetDetailView.as_view(),name="detail"),#/tweet/1
    path('<int:pk>/update',TweetUpdateView.as_view(),name="update"),#/tweet/1/update
    path('<int:pk>/delete',TweetDeleteView.as_view(),name="delete"),#/tweet/1/delete


]