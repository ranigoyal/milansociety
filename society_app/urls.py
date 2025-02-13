from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_member, name='register'),
    path('success/', views.success_page, name='success'),
]
