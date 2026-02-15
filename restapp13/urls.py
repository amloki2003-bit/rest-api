from django.urls import path
from restapp13 import views

urlpatterns = [
    path('studentapi/',views.StudentListView.as_view()),
]
