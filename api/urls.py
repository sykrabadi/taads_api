from django.urls import path, register_converter
from . import views


urlpatterns = [
    path("users/", views.UsersList.as_view()),
    path("stations/", views.StationsList.as_view()),
    path("cycles/", views.CyclesList.as_view()),
]