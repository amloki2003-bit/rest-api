from django.urls import path,include
from restapp11 import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('managerviewset',views.ManagerModelViewSet,basename='manager')

urlpatterns = [
    path('',include(router.urls)),
    path('authentication/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',obtain_auth_token),
]



