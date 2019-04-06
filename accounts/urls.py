from django.urls import path
from .views import UserDetailView

urlpatterns=[

    path('<username>',UserDetailView.as_view(),name='account')
]