from django.contrib import admin
from django.urls import path
from emprestimo_livros import views

urlpatterns = [
    path('update/', views.update_status)
]