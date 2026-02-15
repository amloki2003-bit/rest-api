from django.urls import path,include
from restapp9 import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('customerviewset',views.CustomverViewSet,basename='customer')

urlpatterns = [
    path('',include(router.urls)),
]



