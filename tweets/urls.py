from django.urls import path

from .views import (
    TweetDetailView,
    TweetListView,
    TweetCreateView
)

urlpatterns=[
    path('',TweetListView.as_view(),name="list"), #/tweet/

    path('create/',TweetCreateView.as_view(),name="create"),#/tweet/create
    path('<int:pk>/',TweetDetailView.as_view(),name="detail"),#/tweet/1


]