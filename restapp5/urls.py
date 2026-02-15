from django.urls import path
from restapp5 import views

urlpatterns = [
    path('trainerapi/',views.trainer_api),
]
