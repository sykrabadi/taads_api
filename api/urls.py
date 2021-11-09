from django.urls import path, register_converter
from . import views


urlpatterns = [
    path("users/", views.get_user),
    path("users/<int:pk>", views.get_user_by_id),
    path("users/register/", views.register),
    path("users/delete/<int:pk>", views.delete_user),
    path("station/", views.get_station),
    path("cycle/", views.get_cycle)
]