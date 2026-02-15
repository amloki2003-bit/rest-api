from django.urls import path
from restapp4 import views

urlpatterns = [
    path('employee/',views.EmployeeView.as_view()),
]
