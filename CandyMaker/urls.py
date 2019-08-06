from django.contrib import admin
from django.urls import path
from . import views

app_name = 'CandyMaker'
urlpatterns = [
    path('startmaker/<str:param>/', views.startmaker, name='startmaker'),
]

