from django.urls import path
from restapp1 import views

urlpatterns = [
    path('',views.EmployeeView.as_view()),
]
