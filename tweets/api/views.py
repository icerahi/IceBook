from django.db.models import Q
from rest_framework import permissions

from rest_framework.generics import ListAPIView,CreateAPIView

from tweets.api.serializers import TweetModelSerializer
from tweets.models import Tweet


class TweetCreateAPIView(CreateAPIView):
    serializer_class= TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tweet.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TweetListAPIView(ListAPIView):

    serializer_class = TweetModelSerializer

    def get_queryset(self,*args,**kwargs):

        qs=Tweet.objects.all().order_by('-timestamp')
        query=self.request.GET.get('q',None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query)|
                Q(user__username__icontains=query)
            )
        return qs

