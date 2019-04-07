from django.urls import path
from .views import (
    UserDetailView,
    UserFollowView,
)

urlpatterns=[

    path('<username>/',UserDetailView.as_view(),name='detail'),

    path('<username>/follow/',UserFollowView.as_view(),name='follow')
]