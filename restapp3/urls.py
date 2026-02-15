from django.urls import path
from restapp3 import views

urlpatterns = [
    path('manager/',views.manager_view),
]
