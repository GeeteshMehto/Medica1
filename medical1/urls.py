from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.index, name='contact'),
    path('breastc/', views.index, name='breastc'),
]
