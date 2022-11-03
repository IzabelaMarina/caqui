"""Caqui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from flight_management import views as flightmanagementviews
from flight_monitoring import views as flightmonitoringviews
from login import views as loginviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud', flightmanagementviews.flightmanagementview),
    path('update', flightmanagementviews.flightupdateview),
    path('report/', include('report.urls')),
    path('', loginviews.loginview),
    path('home', flightmonitoringviews.flightmonitoringview),
    path('update/edit', flightmanagementviews.update_status),
]

urlpatterns += [
    path('flightmanagement/', include('flight_management.urls')),
]