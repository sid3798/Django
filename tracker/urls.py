from django.contrib import admin
from django.urls import path
from tracker import views as tracker_views


urlpatterns =[
    path('home/',tracker_views.home,name="home"),
    path('reports/',tracker_views.reports,name="reports"),
    path('patients/',tracker_views.patients,name="patients"),
    
]