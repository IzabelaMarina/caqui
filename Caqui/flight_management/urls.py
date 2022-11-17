from django.urls import path

from . import views

urlpatterns = [
    path('../home', views.index, name='index'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user-detail'),
    path('user/', views.UserListView.as_view(), name='user'),
    path('flight/<int:pk>', views.FlightDetailView.as_view(), name='flight-detail'),
    path('flight/', views.FlightListView.as_view(), name='flight'),

]

# Add URLConf to create, update, and delete authors
urlpatterns += [
    path('user/create/', views.UserCreate.as_view(), name='user-create'),
    path('user/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('flight/create/', views.create_flight, name='flight-create'),
    path('flight/<int:pk>/update/', views.update_flight, name='flight-update'),
    path('flight/<int:pk>/delete/', views.FlightDelete.as_view(), name='flight-delete'),
]

urlpatterns += [
    path('flightstatus/<int:pk>/update/', views.update_status, name='flightstatus-update'),
    path('flightstatus/', views.flightupdateview, name='flightstatus'),
]
