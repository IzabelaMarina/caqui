from django.urls import path
from report import views

urlpatterns = [
    path('', views.ReportView.as_view()),
    path('flightreport', views.reportflightview),
    path('export-pdf', views.export_pdf),
    path('export-pdf-cmpny', views.export_pdf_cmpny),
]