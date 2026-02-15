from django.urls import path
from restapp7 import views

urlpatterns = [
    # path('c/',views.CustomerCreateView.as_view()),
    # path('l/',views.CustomerListView.as_view()),
    # path('r/<int:pk>',views.CustomerRetriveView.as_view()),
    # path('u/<int:pk>',views.CustomerUpdateView.as_view()),
    # path('d/<int:pk>',views.CustomerDestraoyView.as_view()),

    path('lc/',views.CustomerListCreateView.as_view()),
    path('rud/<int:pk>',views.CustomerRetrieveUpdateDestraoyView.as_view()),
]
