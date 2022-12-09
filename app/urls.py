
from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
    path("register/",register_user,name="register_user"),
    path("login/",login_user,name="login_user"),
    path("logout/",logout_user,name="logout_user"),
    path("dashboard/",dashboard,name="dashboard")
]
