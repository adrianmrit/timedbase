from django.urls import path

from . import views

urlpatterns = [
    path('add_watch/', views.add_watch_view, name='api_add_watch'),
]