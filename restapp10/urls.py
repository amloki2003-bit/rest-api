from django.urls import path,include
from restapp10 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('managerviewset',views.ManagerModelViewSet,basename='manager')

urlpatterns = [
    path('',include(router.urls)),
]



