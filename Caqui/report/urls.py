from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReportView.as_view()),
    path('data', views.flight_data, name = 'flight_data'),
    path('flightreport', views.reportflightview),
]