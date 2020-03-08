from django.urls import path

from . import views

urlpatterns = [
    path('add_watch/', views.AddWatchView.as_view(), name='api_add_watch'),
]