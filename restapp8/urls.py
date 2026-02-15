from django.urls import path
from restapp8 import views

urlpatterns = [
    path('c/',views.CustomerCreateView.as_view()),
    path('l/',views.CustomerListView.as_view()),
    path('u/<int:pk>',views.CustomerUpdateView.as_view()),
    path('d/<int:pk>',views.CustomerDestroyView.as_view()),
    path('r/<int:pk>',views.CustomerRetrieveView.as_view()),
    path('lc/',views.CustomerListCreateView.as_view()),
    path('ru/<int:pk>',views.CustomerRetrieveUpdateView.as_view()),
    path('rd/<int:pk>',views.CustomerRetrieveDestraoyView.as_view()),
    path('rud/<int:pk>',views.CustomerRetrieveUpdateDestraoyView.as_view()),
]
