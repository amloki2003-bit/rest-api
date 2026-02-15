from django.urls import path
from restapp6 import views

urlpatterns = [
    path('',views.ManagerView.as_view()),
    path('manager/<int:pk>',views.ManagerView.as_view()),
]
