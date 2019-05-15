from django.contrib import admin

# Register your models here.
from tweets.models import Tweet
from tweets.forms import TweetModelForm

class TweetModelAdmin(admin.ModelAdmin):
   # form = TweetModelForm

    class Meta:
        model=Tweet

admin.site.register(Tweet,TweetModelAdmin)
