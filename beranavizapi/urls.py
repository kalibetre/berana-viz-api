"""
beranavizapi URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

API_BASE_URL = "api/v1/"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_BASE_URL, include('core.urls')),
    path(API_BASE_URL, include('documents.urls')),
]
