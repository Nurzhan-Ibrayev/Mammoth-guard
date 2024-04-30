from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("reg/", views.registerPage),
    path("login/", views.loginPage),
    path("logout/", views.logoutPage),

]
