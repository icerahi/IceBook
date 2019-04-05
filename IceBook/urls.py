from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from tweets.views import TweetListView

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TweetListView.as_view(),name='home'),
    path('tweet/',include(('tweets.urls','tweets'),namespace='tweet')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)