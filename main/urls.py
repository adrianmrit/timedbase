from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('brands/', views.BrandsView.as_view(), name='brands'),
    path('brands/<str:letter>/', views.BrandsView.as_view(), name='brands'),
    path('brand/<int:id>/', views.BrandView.as_view(), name='brand'),
    path('watch/<int:id>/', views.WatchView.as_view(), name='watch'),
]