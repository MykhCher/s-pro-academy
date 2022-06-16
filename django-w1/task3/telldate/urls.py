from django.urls import path
from. import views

urlpatterns = [
    path('', views.telldate),
    path('year/', views.tellyear),
    path('month/', views.tellmonth),
    path('day/', views.tellday)
]
#urls