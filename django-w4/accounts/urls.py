from django.urls import path
from .views import RegisterFromView, LoginFromView, LogoutFromView

urlpatterns = [
    path('register', RegisterFromView.as_view(), name='register'),
    path('login', LoginFromView.as_view(), name='login'),
    path('logout', LogoutFromView.as_view(), name='logout')
]