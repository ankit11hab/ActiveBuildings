from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPollutants, name='get_pollutants'),
]
