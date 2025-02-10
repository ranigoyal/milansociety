from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_member, name='register'),
    path('success/', views.success_page, name='success'),
]
