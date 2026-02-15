from django.urls import path
from restapp12 import views

urlpatterns = [
    path('studentapi/',views.StudentListView.as_view()),
]
