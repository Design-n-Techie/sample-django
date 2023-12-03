# djangotemplates/example/urls.py

from django.urls import path
from example import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'), # Notice the URL has been named
    path('about/', views.AboutPageView.as_view(), name='about'),
]