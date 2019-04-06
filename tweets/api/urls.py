from django.urls import path
from django.views.generic import RedirectView

from .views import (
    TweetListAPIView,
    TweetCreateAPIView)

urlpatterns=[
    #path('',RedirectView.as_view(url='/')), #/redirect/

    path('',TweetListAPIView.as_view(),name="list"), #api/tweet/
    path('create/',TweetCreateAPIView.as_view(),name="create"), #api/tweet/


]