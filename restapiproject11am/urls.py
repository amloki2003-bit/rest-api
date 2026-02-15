"""
URL configuration for restapiproject11am project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restapp1/',include('restapp1.urls')),
    path('restapp2/',include('restapp2.urls')),
    path('restapp3/',include('restapp3.urls')),
    path('restapp4/',include('restapp4.urls')),
    path('restapp5/',include('restapp5.urls')),
    path('restapp6/',include('restapp6.urls')),
    path('restapp7/',include('restapp7.urls')),
    path('restapp8/',include('restapp8.urls')),
    path('restapp9/',include('restapp9.urls')),
    path('restapp10/',include('restapp10.urls')),
    path('restapp11/',include('restapp11.urls')),
    path('restapp12/',include('restapp12.urls')),
    path('restapp13/',include('restapp13.urls')),
    path('',include('restapp14.urls')),

]
