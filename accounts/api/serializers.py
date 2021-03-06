from django.urls import reverse_lazy
from rest_framework import serializers
from django.contrib.auth.models import User



class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count=serializers.SerializerMethodField()
    url=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'follower_count',
            'url'
           # 'email',
        ]
    def get_follower_count(self,obj):
        return 0

    def get_url(self,obj):
        return reverse_lazy('profiles:detail',kwargs={'username':obj.username})