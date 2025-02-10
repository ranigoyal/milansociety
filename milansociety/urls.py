from django.contrib import admin
from django.urls import path, include
from society_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('society/', include('society_app.urls')),
    path('', home, name='home'),  # Add home page URL
]
