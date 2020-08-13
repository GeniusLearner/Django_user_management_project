from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
