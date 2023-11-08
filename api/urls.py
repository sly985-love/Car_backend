
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from api import views


urlpatterns = [
    path('login/', views.LoginView.as_view()),
]
