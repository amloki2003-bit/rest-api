from django.urls import path
from restapp2 import views

urlpatterns = [
    path('emp/<int:pk>',views.get_emp_data),
    path('empall/',views.get_all_emp),
]
