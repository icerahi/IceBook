
from django.contrib.auth.models import User

from django.test import TestCase

# Create your tests here.
from django.urls import reverse

from tweets.models import Tweet


class TweetModelTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create(username="imran")

    def test_tweet_item(self):
        obj=Tweet.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )
        self.assertTrue(obj.content=="Some random content")
        self.assertTrue(obj.id==1)
        absolute_url=reverse("tweet:detail",kwargs={"pk":1})
        self.assertTrue(obj.get_absolute_url(),absolute_url)

    def test_tweet_url(self):
        obj=Tweet.objects.create(
            user=User.objects.first(),
            content="Some random content"
        )
        absolute_url=reverse("tweet:detail",kwargs={"pk":1})
        self.assertTrue(obj.get_absolute_url(),absolute_url)
