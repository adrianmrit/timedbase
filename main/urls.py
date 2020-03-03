from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brands/', views.brands, name='brands'),
    path('brands/<str:letter>/', views.brands, name='brands'),
    path('brand/<int:id>/', views.brand, name='brand'),
    path('watch/<int:id>/', views.watch, name='watch'),
]